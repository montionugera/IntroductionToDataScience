__author__ = 'montionugera'
from pandas import DataFrame, Series


#################
# Syntax Reminder:
#
# The following code would create a two-column pandas DataFrame
# named df with columns labeled 'name' and 'age':
#
# people = ['Sarah', 'Mike', 'Chrisna']
# ages  =  [28, 32, 25]
# df = DataFrame({'name' : Series(people),
#                 'age'  : Series(ages)})

def create_dataframe():
    '''
    Create a pandas dataframe called 'olympic_medal_counts_df' containing
    the data from the table of 2014 Sochi winter olympics medal counts.

    The columns for this dataframe should be called
    'country_name', 'gold', 'silver', and 'bronze'.

    There is no need to  specify row indexes for this dataframe
    (in this case, the rows will automatically be assigned numbered indexes).

    You do not need to call the function in your code when running it in the
    browser - the grader will do that automatically when you submit or test it.
    '''

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

    # your code here
    data = {"country": Series(countries),
            "gold": Series(gold),
            "silver": Series(silver),
            "bronze": Series(bronze)
            }
    olympic_medal_counts_df = DataFrame(data)
    return olympic_medal_counts_df


df = olympic_medal_counts_df = create_dataframe()
# print olympic_medal_counts_df
# print olympic_medal_counts_df.dtypes

olympic_medal_counts_df["gold"]
olympic_medal_counts_df[["gold", "silver"]]
df.loc[0]

df['country'][df['silver'] > 4]

import pandas as pd

'''
You can think of a DataFrame as a group of Series that share an index.
This makes it easy to select specific columns that you want from the
DataFrame.

Also a couple pointers:
1) Selecting a single column from the DataFrame will return a Series
2) Selecting multiple columns from the DataFrame will return a DataFrame

*This playground is inspired by Greg Reda's post on Intro to Pandas Data Structures:
http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
'''
# Change False to True to see Series indexing in action
if False:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print football['year']
    print ''
    print football.year  # shorthand for football['year']
    print ''
    print football[['year', 'wins', 'losses']]

'''
Row selection can be done through multiple ways.

Some of the basic and common methods are:
   1) Slicing
   2) An individual index (through the functions iloc or loc)
   3) Boolean indexing

You can also combine multiple selection requirements through boolean
operators like & (and) or | (or)
'''
# Change False to True to see boolean indexing in action
if True:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    import numpy as np
    # print football.iloc[[0]]
    # print ""
    # print football.loc[[0]]
    # print ""
    # print football[3:5]
    # print ""
    # print football[football.wins > 10]
    # print ""
    # print football[(football.wins > 10) & (football.team == "Packers")]
    # print football[['wins','losses']].apply(np.average)
    # print football[['wins','losses']].apply(np.mean)
    # print football[football.wins > 10]["wins"].map(lambda x: x >= 10)

    # print football[football.wins > 10].applymap(lambda x: x >= 10)


def get_avg_dataframe_atleast_one():
    df = create_dataframe()
    # your code here
    # data = {"country": Series(countries),
    #         "gold": Series(gold),
    #         "silver": Series(silver),
    #         "bronze": Series(bronze)
    #         }
    avg_bronze = df[df.gold >= 1][['bronze']].apply(np.average).bronze
    return avg_bronze


# print get_avg_dataframe_atleast_one()

def get_avg_all_atleast_one_of_any():
    df = create_dataframe()
    # your code here
    # data = {"country": Series(countries),
    #         "gold": Series(gold),
    #         "silver": Series(silver),
    #         "bronze": Series(bronze)
    #         }
    # print(df[df.gold >= 1 | df.silver >= 1 | df.bronze >= 1])
    avg_bronze = df[(df.gold >= 1) | (df.silver >= 1) | (df.bronze >= 1)][['gold', 'silver', 'bronze']].apply(
        np.mean)
    return avg_bronze


# print get_avg_all_atleast_one_of_any()

