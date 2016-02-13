import os

__author__ = 'montionugera'
from pandas import *
import numpy

def imputation(filename):
    # Pandas dataframes have a method called 'fillna(value)', such that you can
    # pass in a single value to replace any NAs in a dataframe or series. You
    # can call it like this:
    #     dataframe['column'] = dataframe['column'].fillna(value)
    #
    # Using the numpy.mean function, which calculates the mean of a numpy
    # array, impute any missing values in our Lahman baseball
    # data sets 'weight' column by setting them equal to the average weight.
    #
    # You can access the 'weight' colum in the baseball data frame by
    # calling baseball['weight']

    baseball = pandas.read_csv(filename)
    print baseball.__class__.__name__
    mw = baseball['weight'].mean()
    #YOUR CODE GOES HERE
    #print baseball['weight']
    baseball['weight']=baseball['weight'].fillna(mw)

    return baseball[['nameGiven','weight']]

current_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(current_path,'data/Master.csv')
print imputation(path)