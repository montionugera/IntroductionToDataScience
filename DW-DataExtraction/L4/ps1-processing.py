import os

__author__ = 'montionugera'
# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with another type of infobox data, audit it, clean it,
come up with a data model, insert it into a MongoDB and then run some queries against your database.
The set contains data about Arachnid class.
Your task in this exercise is to parse the file, process only the fields that are listed in the
FIELDS dictionary as keys, and return a list of dictionaries of cleaned values.

The following things should be done:
- keys of the dictionary changed according to the mapping in FIELDS dictionary
- trim out redundant description in parenthesis from the 'rdf-schema#label' field, like "(spider)"
- if 'name' is "NULL" or contains non-alphanumeric characters, set it to the same value as 'label'.
- if a value of a field is "NULL", convert it to None
- if there is a value in 'synonym', it should be converted to an array (list)
  by stripping the "{}" characters and splitting the string on "|". Rest of the cleanup is up to you,
  eg removing "*" prefixes etc. If there is a singular synonym, the value should still be formatted
  in a list.
- strip leading and ending whitespace from all fields, if there is any
- the output structure should be as follows:
{ 'label': 'Argiope',
  'uri': 'http://dbpedia.org/resource/Argiope_(spider)',
  'description': 'The genus Argiope includes rather large and spectacular spiders that often ...',
  'name': 'Argiope',
  'synonym': ["One", "Two"],
  'classification': {
                    'family': 'Orb-weaver spider',
                    'class': 'Arachnid',
                    'phylum': 'Arthropod',
                    'order': 'Spider',
                    'kingdom': 'Animal',
                    'genus': None
                    }
}
  * Note that the value associated with the classification key is a dictionary with
    taxonomic labels.
"""
{'synonym': None, 'name': 'Argiope',
 'classification': {'kingdom': 'Animal', 'phylum': 'Arthropod', 'class': 'Arachnid', 'family': 'Orb-weaver spider',
                    'order': 'Spider'}, 'omment': 'The', 'uri': 'http://dbpedia.org/resource/Argiope_(spider)',
 'label': 'Argiope', 'genus_label': None}
import codecs
import csv
import json
import pprint
import re

current_path = os.path.dirname(os.path.realpath(__file__))

DATAFILE = os.path.join(current_path, 'arachnid.csv')
FIELDS = {'rdf-schema#label': 'label',
          'URI': 'uri',
          'rdf-schema#comment': 'description',
          'synonym': 'synonym',
          'name': 'name',
          'family_label': 'family',
          'class_label': 'class',
          'phylum_label': 'phylum',
          'order_label': 'order',
          'kingdom_label': 'kingdom',
          'genus_label': 'genus'}


def process_file(filename, fields):
    process_fields = fields.keys()
    data = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for i in range(3):
            l = reader.next()

        for line in reader:
            # YOUR CODE HERE
            row_data = {}
            for field in FIELDS:
                val = line[field]
                field = field.lower()
                # - trim out redundant description in parenthesis from the 'rdf-schema#label' field, like "(spider)"
                if field.startswith("rdf-schema#"):
                    if field == 'rdf-schema#label':
                        val = val.split("(")[0]
                    field = field.split("#")[1]
                    val = val.strip(" ")

                # - strip leading and ending whitespace from all fields, if there is any
                val = val.strip(" ")
                # - if 'name' is "NULL" or contains non-alphanumeric characters, set it to the same value as 'label'.
                # - if a value of a field is "NULL", convert it to None
                if val is None or val == "NULL" or val == "":
                    val = None
                # - if there is a value in 'synonym', it should be converted to an array (list)
                #   by stripping the "{}" characters and splitting the string on "|". Rest of the cleanup is up to you,
                #   eg removing "*" prefixes etc. If there is a singular synonym, the value should still be formatted
                #   in a list.
                if field == 'synonym':
                    if val is None:
                        row_data[field] = val
                        continue
                    val = val.strip("{}")
                    vals = val.split("|")
                    val_list = [val.lstrip("*") for val in vals]
                    row_data[field] = val_list
                    continue
                if field.endswith("_label"):
                    field = field.rstrip("_label")
                    val_dict = row_data.get("classification", {})
                    val_dict[field] = val
                    row_data["classification"] = val_dict
                    continue
                if field in ['label', 'uri', 'description', 'name', 'synonym', 'classification']:
                    row_data[field] = val
                else:
                    if field == 'comment':
                        row_data['description'] = val
            pprint.pprint(row_data, width=1)
            if row_data['name'] is None:
                row_data['name'] = row_data['label']
            data.append(row_data)

    return data


def parse_array(v):
    if (v[0] == "{") and (v[-1] == "}"):
        v = v.lstrip("{")
        v = v.rstrip("}")
        v_array = v.split("|")
        v_array = [i.strip() for i in v_array]
        return v_array
    return [v]


def test():
    data = process_file(DATAFILE, FIELDS)
    print("------------##########")
    print "Your first entry:"
    pprint.pprint(data[0])
    first_entry = {
        "synonym": None,
        "name": "Argiope",
        "classification": {
            "kingdom": "Animal",
            "family": "Orb-weaver spider",
            "order": "Spider",
            "phylum": "Arthropod",
            "genus": None,
            "class": "Arachnid"
        },
        "uri": "http://dbpedia.org/resource/Argiope_(spider)",
        "label": "Argiope",
        "description": "The genus Argiope includes rather large and spectacular spiders that often have a strikingly coloured abdomen. These spiders are distributed throughout the world. Most countries in tropical or temperate climates host one or more species that are similar in appearance. The etymology of the name is from a Greek name meaning silver-faced."
    }

    assert len(data) == 76
    assert data[0] == first_entry
    assert data[17]["name"] == "Ogdenia"
    assert data[48]["label"] == "Hydrachnidiae"
    assert data[14]["synonym"] == ["Cyrene Peckham & Peckham"]


if __name__ == "__main__":
    test()
