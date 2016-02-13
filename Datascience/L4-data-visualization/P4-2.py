import os
from time import strftime
import numpy as np

__author__ = 'montionugera'
import pandas
from ggplot import *


def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather.
    focused on the MTA and weather data we used in assignment #3.
    You should feel free to implement something that we discussed in class
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.
    '''
    # ,UNIT,DATEn,TIMEn,Hour,DESCn,ENTRIESn_hourly,EXITSn_hourly,\
    # maxpressurei,maxdewpti,mindewpti,minpressurei,meandewpti,meanpressurei,\
    # fog,rain,meanwindspdi,mintempi,meantempi,maxtempi,precipi,thunder
    # 2011-05-01,01:00:00
    # %Y-%m-%d %H:%M:%S

    # check by time
    turnstile_weather['dttm'] = pandas.to_datetime(turnstile_weather.DATEn + " " + turnstile_weather.TIMEn,
                                                   format='%Y-%m-%d %H:%M:%S')
    # turnstile_weather['week_day'] = turnstile_weather['dttm'].apply(lambda dttm: strftime('%w', dttm.date))
    turnstile_weather['week_day'] = turnstile_weather['dttm'].apply(lambda x: x.dayofweek)
    turnstile_weather['week_hour'] = turnstile_weather['week_day']*24 + turnstile_weather['Hour']
    # rain_avg_entries =
    # agg = turnstile_weather.groupby(['rain', 'week_hour'], as_index=False).mean()
    agg = turnstile_weather.groupby(['week_day','Hour'], as_index=False).mean()
    # agg['UNIT'] = agg[agg.index.levels]
    print agg

    gg = ggplot(agg, aes('Hour', 'ENTRIESn_hourly', color='week_day')) + \
         geom_point() + ggtitle('ENTRIESn_hourly by Time') +\
         geom_line()+\
         xlab('Hour') + ylab('ENTRIESn_hourly')
    return gg


# ggplot(dat, aes(x=Member, y=Percentage, fill = factor(Percentage))) + geom_bar(stat = "identity")
current_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(current_path, 'turnstile_data_master_with_weather.csv')
turnstile_weather = pandas.read_csv(filename)
gg = plot_weather_data(turnstile_weather)
print gg
