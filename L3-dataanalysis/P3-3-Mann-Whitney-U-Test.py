import os
import numpy as np
import scipy
import scipy.stats
import pandas

def mann_whitney_plus_means(turnstile_weather):
    '''
    This function will consume the turnstile_weather dataframe containing
    our final turnstile weather data. 
    
    You will want to take the means and run the Mann Whitney U-test on the 
    ENTRIESn_hourly column in the turnstile_weather dataframe.
    
    This function should return:
        1) the mean of entries with rain
        2) the mean of entries without rain
        3) the Mann-Whitney U-statistic and p-value comparing the number of entries
           with rain and the number of entries without rain
    
    You should feel free to use scipy's Mann-Whitney implementation, and you 
    might also find it useful to use numpy's mean function.
    
    Here are the functions' documentation:
    http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    
    You can look at the final turnstile weather data at the link below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
    
    ### YOUR CODE HERE ###
    rain_df = turnstile_weather[turnstile_weather.rain == 1]['ENTRIESn_hourly']
    norain_df = turnstile_weather[turnstile_weather.rain == 0]['ENTRIESn_hourly']
    without_rain_mean = np.mean(norain_df)
    with_rain_mean = np.mean(rain_df)
    U,p = scipy.stats.mannwhitneyu(rain_df,norain_df)
    return with_rain_mean, without_rain_mean, U, p # leave this line for the grader

current_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(current_path,'turnstile_data_master_with_weather.csv')
turnstile_weather = pandas.read_csv(filename)

print mann_whitney_plus_means(turnstile_weather)
'''
t-test is mannwhitneyu method to test null hypothesis, and
the p result is 0.025 which less than  p-critical 0.05,
So we can conclude that there are different "ENTRIESn_hourly"
between without rain and with rain day.'''