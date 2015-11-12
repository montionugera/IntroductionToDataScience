import os
import numpy as np
import pandas
import matplotlib.pyplot as plt
import time


def entries_histogram(turnstile_weather):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, let's 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Let's plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()
    
    Your histogram may look similar to bar graph in the instructor notes below.
    
    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
    
    You can see the information contained within the turnstile weather data here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
    
    plt.figure()
    # your code here to plot a historgram for hourly entries when it is raining
    rain_df = turnstile_weather[turnstile_weather.rain == 1]['ENTRIESn_hourly']
    # your code here to plot a historgram for hourly entries when it is not raining
    norain_df = turnstile_weather[turnstile_weather.rain == 0]['ENTRIESn_hourly']
    # print len(norain_df)
    # print len(rain_df)
    df_compare = pandas.DataFrame({'rain': rain_df,
                   'no_rain': norain_df})
    df_compare.plot(kind='hist', alpha=0.2)
    #,UNIT,DATEn,TIMEn,Hour,DESCn,ENTRIESn_hourly,EXITSn_hourly,maxpressurei
    # turnstile_weather['index'] = turnstile_weather.index.values
    # print turnstile_weather['index']
    # turnstile_weather.plot(kind='scatter',x = 'index', y='ENTRIESn_hourly')
    return plt
current_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(current_path,'turnstile_data_master_with_weather.csv')
turnstile_weather = pandas.read_csv(filename)
plt.ion()
entries_histogram(turnstile_weather)
plt.show(block=False)
time.sleep(10)
print 'asdasdasd'
plt.close()
#http://stackoverflow.com/questions/11140787/closing-pyplot-windows
#
# Does the data seem normally distributed?
# no
# Do you think we would be able to use Welch's t-test on this data?
# yes