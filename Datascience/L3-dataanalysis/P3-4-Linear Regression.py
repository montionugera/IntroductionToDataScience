import os

__author__ = 'montionugera'
import numpy as np
import pandas
from ggplot import *

"""
In this question, you need to:
1) implement the compute_cost() and gradient_descent() procedures
2) Select features (in the predictions procedure) and make predictions.

"""


def normalize_features(df):
    """
    Normalize the features in the data set.
    """
    mu = df.mean()
    sigma = df.std()

    if (sigma == 0).any():
        raise Exception("One or more features had the same value for all samples, and thus could " + \
                        "not be normalized. Please do not include features with only a single value " + \
                        "in your model.")
    df_normalized = (df - df.mean()) / df.std()

    return df_normalized, mu, sigma


def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values,
    and the values for our thetas.

    This can be the same code as the compute_cost function in the lesson #3 exercises,
    but feel free to implement your own.
    """

    m = len(values)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2 * m)

    return cost


def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.

    This can be the same gradient descent code as in the lesson #3 exercises,
    but feel free to implement your own.
    """

    m = len(values)
    cost_history = []

    for i in range(num_iterations):
        theta = theta - (alpha / len(values)) * np.dot(np.dot(features, theta) - values, features)
        cost = compute_cost(features, values, theta)
        cost_history.append(cost)
    return theta, pandas.Series(cost_history)


def predictions(dataframe):
    '''
    The NYC turnstile data is stored in a pandas dataframe called weather_turnstile.
    Using the information stored in the dataframe, let's predict the ridership of
    the NYC subway using linear regression with gradient descent.

    You can download the complete turnstile weather dataframe here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

    Your prediction should have a R^2 value of 0.40 or better.
    You need to experiment using various input features contained in the dataframe.
    We recommend that you don't use the EXITSn_hourly feature as an input to the
    linear model because we cannot use it as a predictor: we cannot use exits
    counts as a way to predict entry counts.

    Note: Due to the memory and CPU limitation of our Amazon EC2 instance, we will
    give you a random subet (~15%) of the data contained in
    turnstile_data_master_with_weather.csv. You are encouraged to experiment with
    this computer on your own computer, locally.


    If you'd like to view a plot of your cost history, uncomment the call to
    plot_cost_history below. The slowdown from plotting is significant, so if you
    are timing out, the first thing to do is to comment out the plot command again.

    If you receive a "server has encountered an error" message, that means you are
    hitting the 30-second limit that's placed on running your program. Try using a
    smaller number for num_iterations if that's the case.

    If you are using your own algorithm/models, see if you can optimize your code so
    that it runs faster.
    '''
    turnstile_weather['dttm'] = pandas.to_datetime(turnstile_weather.DATEn + " " + turnstile_weather.TIMEn,
                                                   format='%Y-%m-%d %H:%M:%S')
    turnstile_weather['week'] =  turnstile_weather['dttm'].apply(lambda x: x.dayofweek)
    print turnstile_weather['week']
    turnstile_weather['week0'] = turnstile_weather['dttm'].apply(lambda x: x.dayofweek == 0)
    turnstile_weather['week1'] = turnstile_weather['dttm'].apply(lambda x: x.dayofweek == 1)
    turnstile_weather['week2'] = turnstile_weather['dttm'].apply(lambda x: x.dayofweek == 2)
    turnstile_weather['week3'] = turnstile_weather['dttm'].apply(lambda x: x.dayofweek == 3)
    turnstile_weather['week4'] = turnstile_weather['dttm'].apply(lambda x: x.dayofweek == 4)
    turnstile_weather['week5'] = turnstile_weather['dttm'].apply(lambda x: x.dayofweek == 5)
    turnstile_weather['week6'] = turnstile_weather['dttm'].apply(lambda x: x.dayofweek == 6)

    # Select Features (try different features!)
    features = dataframe[['rain', 'precipi', 'Hour', 'meantempi', 'week0', 'week1', 'week2', 'week3', 'week4', 'week5', 'week6']]

    # Add UNIT to features using dummy variables
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    features = features.join(dummy_units)
    print features
    # Values
    values = dataframe['ENTRIESn_hourly']
    m = len(values)

    features, mu, sigma = normalize_features(features)
    features['ones'] = np.ones(m)  # Add a column of 1s (y intercept)

    # Convert features and values to numpy arrays
    features_array = np.array(features)
    values_array = np.array(values)

    # Set values for alpha, number of iterations.
    alpha = 0.1  # please feel free to change this value
    num_iterations = 50  # please feel free to change this value

    # Initialize theta, perform gradient descent
    theta_gradient_descent = np.zeros(len(features.columns))
    theta_gradient_descent, cost_history = gradient_descent(features_array,
                                                            values_array,
                                                            theta_gradient_descent,
                                                            alpha,
                                                            num_iterations)
    # -------------------------------------------------
    # Uncomment the next line to see your cost history
    # -------------------------------------------------
    plot = plot_cost_history(alpha, cost_history)
    #
    # Please note, there is a possibility that plotting
    # this in addition to your calculation will exceed
    # the 30 second limit on the compute servers.

    predictions = np.dot(features_array, theta_gradient_descent)
    return predictions, plot


def plot_cost_history(alpha, cost_history):
    """This function is for viewing the plot of your cost history.
    You can run it by uncommenting this

        plot_cost_history(alpha, cost_history)

    call in predictions.

    If you want to run this locally, you should print the return value
    from this function.
    """
    cost_df = pandas.DataFrame({
        'Cost_History': cost_history,
        'Iteration': range(len(cost_history))
    })
    return ggplot(cost_df, aes('Iteration', 'Cost_History')) + \
           geom_point() + ggtitle('Cost History for alpha = %.3f' % alpha)


current_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(current_path, 'turnstile_data_master_with_weather.csv')
turnstile_weather = pandas.read_csv(filename)

predictions_data, plot = predictions(turnstile_weather)

print predictions_data
# Your r^2 value is: 0.463968815042. Good job! Can you make it even better?
print plot
# http://www.slideshare.net/Yhat/ggplot-for-python
import matplotlib.pyplot as plt
def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).
    Try different binwidths for your histogram.

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''

    plt.figure()
    df = (turnstile_weather['ENTRIESn_hourly'] - predictions)
    # df.hist()

    df.plot(kind='hist',alpha=0.2,  y='ENTRIESn_hourly',bins = range(-7500, 7500, 500))

    df = (turnstile_weather['ENTRIESn_hourly'] - turnstile_weather['ENTRIESn_hourly'].mean())
    df.plot(kind='hist',alpha=0.2,  y='ENTRIESn_hourly',bins = range(-7500, 7500, 500) , color="pink")
    return plt


def r_squared(data, predictions):
    SSReg = ((predictions - data) ** 2).sum()
    SST = ((data - np.mean(data)) ** 2).sum()
    print SSReg
    print SST
    r_squared = 1 - SSReg / SST
    return r_squared

print predictions_data

print "r^2 = %s" % r_squared(turnstile_weather['ENTRIESn_hourly'], predictions_data)

plot_residuals(turnstile_weather, predictions_data)
plt.show()
