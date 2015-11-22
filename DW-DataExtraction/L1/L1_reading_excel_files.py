#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""
import os

import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    ### other useful methods:
    print "\nROWS, COLUMNS, and CELLS:"
    print "Number of rows in the sheet:",
    print sheet.nrows
    print "Type of data in cell (row 3, col 2):",
    print sheet.cell_type(3, 2)
    print "Value in cell (row 3, col 2):",
    print sheet.cell_value(3, 2)
    print "Get a slice of values in column 3, from rows 1-3:"
    print sheet.col_values(3, start_rowx=1, end_rowx=4)

    print "\nDATES:"
    print "Type of data in cell (row 1, col 0):",
    print sheet.cell_type(1, 0)
    exceltime = sheet.cell_value(1, 0)
    print "Time in Excel format:",
    print exceltime
    print "Convert time to a Python datetime tuple, from the Excel float:",
    print xlrd.xldate_as_tuple(exceltime, 0)


    data = {
            'maxtime': (0, 0, 0, 0, 0, 0),
            'maxvalue': 0,
            'mintime': (0, 0, 0, 0, 0, 0),
            'minvalue': 0,
            'avgcoast': 0
    }
    maxtime =  None
    mintime =  None
    time_at_max_value = None
    minvalue = -1
    maxvalue = 0
    sum_coast = 0
    for row in range(1,sheet.nrows):
        excel_cols = sheet.row_slice(row,start_colx=0,end_colx=9)
        exceltime = excel_cols[0].value
        sum_coast += excel_cols[1].value
        if maxtime is None:
            maxtime = exceltime
        elif maxtime < exceltime:
            maxtime = exceltime

        maxvalue_row = excel_cols[1].value #max([x.value for x in excel_cols[1:]])
        if maxvalue < maxvalue_row:
            time_at_max_value = excel_cols[0].value
            maxvalue = maxvalue_row

        if minvalue > maxvalue_row or minvalue == -1:
            minvalue = maxvalue_row
            mintime  = excel_cols[0].value

    data['minvalue'] = minvalue
    data['maxvalue'] = maxvalue
    data['avgcoast'] = sum_coast/ (sheet.nrows-1)
    data['maxtime'] = xlrd.xldate_as_tuple(time_at_max_value, 0)
    data['mintime'] = xlrd.xldate_as_tuple(mintime, 0)

    cv = sheet.col_values(1,start_rowx=1,end_rowx=None)
    maxvalue = max(cv)
    minvalue = min(cv)
    maxpos = cv.index(maxvalue)+1
    minpos = cv.index(minvalue)+1
    mintime = sheet.cell_value(minpos,0)



    return data


def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


current_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(current_path,datafile)
parse_file(filename)