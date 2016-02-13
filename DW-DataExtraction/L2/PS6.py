#!/usr/bin/env python
# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.
import os
import xml.etree.ElementTree as ET
current_path = os.path.dirname(os.path.realpath(__file__))
datafile = 'patent2.data'
PATENTS = os.path.join(current_path,datafile)


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()

def create_or_update_newfile(fname,sumstring):
    writing_file = open(fname, "w")
    if writing_file is not None: #write
        writing_file.write(sumstring)
        writing_file.close()



def split_file(filename):
    # we want you to split the input file into separate files
    # each containing a single patent.
    # As a hint - each patent declaration starts with the same line that was causing the error
    # The new files should be saved with filename in the following format:
    writing_file = None
    datafiles = []
    datafile = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("<?xml"):
                datafile = []
                datafiles.append(datafile)
            #collect
            datafile += [line+"\n"]

    n = 0
    for datafile in datafiles:
        fwname = "{}-{}".format(filename, n)
        sumstr = "".join(datafile)
        create_or_update_newfile(fwname,sumstr)
        n += 1


def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)


test()