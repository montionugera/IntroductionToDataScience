#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pprint
import xml.etree.cElementTree as ET
import re
import codecs
import json

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

CREATED = ["version", "changeset", "timestamp", "user", "uid"]


def shape_element(element, record_data={'clean_street': [], 'clean_postcode': [], 'ignore_postcode': []}):
    # In particular the following things should be done:
    # - you should process only 2 types of top level tags: "node" and "way"
    def process_normal_attr(target_element, _node):
        _node['type'] = target_element.tag
        for k in target_element.attrib:
            if k not in CREATED and k not in ['lat', 'lon']:
                _node[k] = target_element.attrib[k]

    # - all attributes of "node" and "way" should be turned into regular key/value pairs, except:
    #     - attributes in the CREATED array should be added under a key "created"

    def process_created(target_element, _node):
        create_dict = {}
        for create_key in CREATED:
            if create_key in target_element.attrib:
                create_dict[create_key] = target_element.attrib[create_key]
        if len(create_dict) > 0:
            _node['created'] = create_dict
        return create_dict

    #     - attributes for latitude and longitude should be added to a "pos" array,
    #       for use in geospacial indexing. Make sure the values inside "pos" array are floats
    #       and not strings.

    def process_geo(target_element, _node):
        pos = []
        for pos_key in ['lat', 'lon']:
            if pos_key in target_element.attrib:
                pos.append(float(target_element.attrib[pos_key]))
        if len(pos) == 2:
            _node["pos"] = pos
        return pos

    # - if second level tag "k" value contains problematic characters, it should be ignored
    # - if there is a second ":" that separates the type/direction of a street,
    #   the tag should be ignored,

    def should_ignore_tag(target_element):
        return problemchars.match(target_element.attrib['k']) or "street:" in target_element.attrib['k']

    def should_ignore_addresss(addresss):
        postcode = addresss.get("postcode", None)
        return postcode is not None and not postcode.startswith("282")

    # - if second level tag "k" value starts with "addr:", it should be added to a dictionary "address"

    def is_address_tag(target_element):
        return target_element.attrib['k'].startswith("addr:")

    street_mapping = {"S": "South",
                      "Ste": "Suite",
                      "St.": "Street",
                      "St": "Street",
                      "Rd": "Road",
                      "Rd.": "Road"
                      }

    def process_address_street_name(street_name):

        for abbv in ["Ste", "St.", "St", "Rd", "Rd.", "S"]:
            if abbv + " " in street_name or street_name.endswith(abbv):
                record_data['clean_street'].append(street_name)
                street_name = street_name.replace(abbv, street_mapping[abbv])
        return street_name

    def process_address_post_code(post_code):

        if re.compile(r'^[a-zA-Z]{2}[0-9]{5}$', re.IGNORECASE).search(post_code):
            record_data['clean_postcode'].append(post_code)
            return post_code[2:]
        if len(post_code) > 5:
            record_data['clean_postcode'].append(post_code)
        return post_code[:5]

    def process_address_tag(target_element, address={}):
        k = target_element.attrib['k'].replace("addr:", "")
        if k == 'street':
            address[k] = process_address_street_name(target_element.attrib['v'])
        elif k == 'postcode':
            address[k] = process_address_post_code(target_element.attrib['v'])
        else:
            address[k] = target_element.attrib['v']
        return address

    # - if second level tag "k" value does not start with "addr:", but contains ":", you can process it
    #   same as any other tag.

    def process_way_sub_element(way_element, _node={}):
        node_refs = []
        for nd in way_element.iter("nd"):
            node_refs.append(nd.attrib['ref'])
        _node["node_refs"] = node_refs

    node = {}
    if element.tag == "node" or element.tag == "way":
        process_normal_attr(element, node)
        process_created(element, node)
        process_geo(element, node)

        address = {}
        for tag in element.iter("tag"):
            if not should_ignore_tag(tag):
                if is_address_tag(tag):
                    process_address_tag(tag, address=address)
                    if should_ignore_addresss(address):
                        record_data['ignore_postcode'].append(address)
                        return None
                else:
                    node[tag.attrib['k']] = tag.attrib['v']
        if len(address) > 0:
            node['address'] = address
        if element.tag == "way":
            process_way_sub_element(element, node)
        return node
    else:
        return None


def process_map(file_in, pretty=False):
    # You do not need to change this file
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2) + "\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data


def process_map(file_in, pretty=False):
    # You do not need to change this file
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2) + "\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data


OSMFILE = 'charlotte.osm'


def grab_set(file_in):
    check_set = set()
    record_data={'clean_street': [], 'clean_postcode': [], 'ignore_postcode': []}
    for _, element in ET.iterparse(file_in):
        el = shape_element(element,record_data=record_data)
        if el is not None:
            check_set.add(el.get('address', {}).get('postcode', ''))
    print 'The records be cleaned street name is : ',str(len(record_data['clean_street'])) ,' records.'
    print 'The records be cleaned postcode is : ',str(len(record_data['clean_postcode'])) ,' records.'
    print 'The records be ignore because postcode does not start with 282 : ',str(len(record_data['ignore_postcode'])) ,' records.'


if __name__ == "__main__":
    data = process_map(OSMFILE, True)
    # data = grab_set(OSMFILE)
