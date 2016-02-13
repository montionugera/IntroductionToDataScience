#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up. In the first exercise we want you to audit
the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- NoneType if the value is a string "NULL" or an empty string ""
- list, if the value starts with "{"
- int, if the value can be cast to int
- float, if the value can be cast to float, but CANNOT be cast to int.
   For example, '3.23e+07' should be considered a float because it can be cast
   as float but int('3.23e+07') will throw a ValueError
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a
SET of the types that can be found in the field. e.g.
{"field1: set([float, int, str]),
 "field2: set([str]),
  ....
}

All the data initially is a string, so you have to do some checks on the values
first.
"""
import codecs
import csv
import json
import os
import pprint

current_path = os.path.dirname(os.path.realpath(__file__))

CITIES = os.path.join(current_path,'cities.csv')
# CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal",
          "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long",
          "areaLand", "areaMetro", "areaUrban"]
def is_str_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
def is_str_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def audit_file(filename, fields):
    fieldtypes = {}
    extypes = {}
    for field in FIELDS:
        fieldtypes[field] = set()
    for field in FIELDS:
        extypes[field] = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        print header
        #skipping the extra metadata
        for i in range(3):
            l = reader.next()
        for readrow in reader:
            for field in FIELDS:
                val = readrow[field]
                #                     - NoneType if the value is a string "NULL" or an empty string ""
                if val is None or val == "NULL" or val == "":
                    val = None
                elif val.startswith("{"):
                    val = []
                elif is_str_int(val):
                    val = 0
                elif is_str_float(val):
                    val = 0.1
                b4Field = fieldtypes[field]
                fieldtypes[field] = fieldtypes[field].union(set([type(val)]))
                if b4Field != fieldtypes[field]:
                    extypes[field].append(readrow[field])

    pprint.pprint(extypes)
    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])

if __name__ == "__main__":
    test()
