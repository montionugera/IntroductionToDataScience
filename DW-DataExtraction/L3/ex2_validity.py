"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014

- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import os
import pprint
from dateutil import parser


current_path = os.path.dirname(os.path.realpath(__file__))

INPUT_FILE = os.path.join(current_path,'autos.csv')
OUTPUT_GOOD =os.path.join(current_path, 'autos-valid.csv')
OUTPUT_BAD = os.path.join(current_path,'FIXME-autos.csv')


def process_file(input_file, output_good, output_bad):
    # productionStartYear
    # year range 1886-2014
    GOOD_DATA = []
    BAD_DATA = []
    ALL_DATA = []
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        #COMPLETE THIS FUNCTION
        head_to_index = dict()
        count = 0
        for head in header:
            head_to_index[head] = count
            count +=1
        for readrow in reader:
            ALL_DATA.append(readrow)
            # - discard rows (neither write to good nor bad) if the URI is not from dbpedia.org

            if not readrow["URI"].startswith("http://dbpedia.org"):
                print " IGNORE %s" % readrow["URI"]
                continue
            # - check if the field "productionStartYear" contains a year
            productionStartYear = readrow["productionStartYear"]
            try:
                parser.parse(productionStartYear)
                year = int(productionStartYear.split('-')[0])

            except ValueError as ev:
                print " Bad dt %s" % productionStartYear
                BAD_DATA.append(readrow)
                continue
            # - check if the year is in range 1886-2014
            if year not in range(1886,2014):
                print " Bad Year %s" % year
                BAD_DATA.append(readrow)
                continue
            print " Good Year %s %s" % (readrow["productionStartYear"] ,year)

            # - convert the value of the field to be just a year (not full datetime)
            readrow["productionStartYear"] = year
            # - the rest of the fields and values should stay the same

            # - if the value of the field is a valid year in the range as described above,
            #   write that line to the output_good file
            GOOD_DATA.append(readrow)

            # - if the value of the field is not a valid year as described above,
            #   write that line to the output_bad file

            # - you should use the provided way of reading and writing data (DictReader and DictWriter)

            #   They will take care of dealing with the header.
    print "%s %s %s"%(len(ALL_DATA),len(GOOD_DATA),len(BAD_DATA))


    # This is just an example on how you can use csv.DictWriter
    # Remember that you have to output 2 files
    with open(output_good, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in GOOD_DATA:
            writer.writerow(row)
    with open(output_bad, "w") as b:
        writer = csv.DictWriter(b, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in BAD_DATA:
            writer.writerow(row)


def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()