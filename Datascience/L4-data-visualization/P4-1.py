import os

__author__ = 'montionugera'
import pandas as pd
from ggplot import *

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather.
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.
    You should feel free to implement something that we discussed in class
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/

    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

    To see all the columns and data points included in the turnstile_weather
    dataframe.

    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
# ,UNIT,DATEn,TIMEn,Hour,DESCn,ENTRIESn_hourly,EXITSn_hourly,\
 # maxpressurei,maxdewpti,mindewpti,minpressurei,meandewpti,meanpressurei,\
 # fog,rain,meanwindspdi,mintempi,meantempi,maxtempi,precipi,thunder
    #2011-05-01,01:00:00
    #%Y-%m-%d %H:%M:%S
    turnstile_weather['dttm'] =  pd.to_datetime(turnstile_weather.DATEn+" "+turnstile_weather.TIMEn, format='%Y-%m-%d %H:%M:%S')
    gg = ggplot(turnstile_weather,aes('Hour','ENTRIESn_hourly', color = 'UNIT'))+ \
           geom_point() + ggtitle('ENTRIESn_hourly by Time') +\
        xlab('Hour')+ylab('ENTRIESn_hourly')
    return gg
#ggplot(dat, aes(x=Member, y=Percentage, fill = factor(Percentage))) + geom_bar(stat = "identity")
current_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(current_path,'turnstile_data_master_with_weather.csv')
turnstile_weather = pd.read_csv(filename)
gg = plot_weather_data(turnstile_weather)
print gg