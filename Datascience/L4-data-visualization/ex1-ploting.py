import os

__author__ = 'montionugera'
from pandas import *
from ggplot import *

import pandas

def lineplot(hr_year_csv):
    # A csv file will be passed in as an argument which
    # contains two columns -- 'HR' (the number of homerun hits)
    # and 'yearID' (the year in which the homeruns were hit).
    #
    # Fill out the body of this function, lineplot, to use the
    # passed-in csv file, hr_year.csv, and create a
    # chart with points connected by lines, both colored 'red',
    # showing the number of HR by year.
    #
    # You will want to first load the csv file into a pandas dataframe
    # and use the pandas dataframe along with ggplot to create your visualization
    #
    # You can check out the data in the csv file at the link below:
    # https://www.dropbox.com/s/awgdal71hc1u06d/hr_year.csv
    #
    # You can read more about ggplot at the following link:
    # https://github.com/yhat/ggplot/

    baseball_stats = pandas.read_csv(hr_year_csv)

    gg = ggplot(baseball_stats,aes('yearID','HR'))+ \
           geom_point(color = 'red') + ggtitle('Total HRs by Year') + geom_line(color='red')+\
        xlab('Year')+ylab('HR')
    return gg


current_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(current_path,'hr_year.csv')
gg = lineplot(filename)
print gg
#https://github.com/yhat/ggplot/