import os
import pandas

from ggplot import *


def lineplot_compare(hr_by_team_year_sf_la_csv):
    # Write a function, lineplot_compare, that will read a csv file
    # called hr_by_team_year_sf_la.csv and plot it using pandas and ggplot.
    #
    # This csv file has three columns: yearID, HR, and teamID. The data in the
    # file gives the total number of home runs hit each year by the SF Giants 
    # (teamID == 'SFN') and the LA Dodgers (teamID == "LAN"). Produce a 
    # visualization comparing the total home runs by year of the two teams. 
    # 
    # You can see the data in hr_by_team_year_sf_la_csv
    # at the link below:
    # https://www.dropbox.com/s/wn43cngo2wdle2b/hr_by_team_year_sf_la.csv
    #
    # Note that to differentiate between multiple categories on the 
    # same plot in ggplot, we can pass color in with the other arguments
    # to aes, rather than in our geometry functions. For example, 
    # ggplot(data, aes(xvar, yvar, color=category_var)). This should help you 
    # in this exercise.

    baseball_stats = pandas.read_csv(hr_by_team_year_sf_la_csv)
    # baseball_stats = baseball_stats[baseball_stats.teamID == 'SFN']
    gg = ggplot(baseball_stats,aes('yearID','HR', color = 'teamID'))+ \
           geom_point() + ggtitle('Total HRs by Year') + geom_line()+\
        xlab('Year')+ylab('HR')
    return gg


current_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(current_path,'hr_by_team_year_sf_la.csv')
gg = lineplot_compare(filename)
print gg
#https://github.com/yhat/ggplot/