import os

__author__ = 'montionugera'
# -*- coding: utf-8 -*-

import numpy as np
import pandas
import scipy
import statsmodels.api as sm
import matplotlib.pyplot as plt
from ggplot import *

"""
In this optional exercise, you should complete the function called
predictions(turnstile_weather). This function takes in our pandas
turnstile weather dataframe, and returns a set of predicted ridership values,
based on the other information in the dataframe.

In exercise 3.5 we used Gradient Descent in order to compute the coefficients
theta used for the ridership prediction. Here you should attempt to implement
another way of computing the coeffcients theta. You may also try using a reference implementation such as:
http://statsmodels.sourceforge.net/devel/generated/statsmodels.regression.linear_model.OLS.html

One of the advantages of the statsmodels implementation is that it gives you
easy access to the values of the coefficients theta. This can help you infer relationships
between variables in the dataset.

You may also experiment with polynomial terms as part of the input variables.

The following links might be useful:
http://en.wikipedia.org/wiki/Ordinary_least_squares
http://en.wikipedia.org/w/index.php?title=Linear_least_squares_(mathematics)
http://en.wikipedia.org/wiki/Polynomial_regression

This is your playground. Go wild!

How does your choice of linear regression compare to linear regression
with gradient descent computed in Exercise 3.5?

You can look at the information contained in the turnstile_weather dataframe below:
https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv

Note: due to the memory and CPU limitation of our amazon EC2 instance, we will
give you a random subset (~10%) of the data contained in turnstile_data_master_with_weather.csv

If you receive a "server has encountered an error" message, that means you are hitting
the 30 second limit that's placed on running your program. See if you can optimize your code so it
runs faster.
"""


class PredictModel(object):
    dataframe = None
    features = None
    values = None

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.features = self._find_features()
        self.values = self.dataframe['ENTRIESn_hourly']

    def _find_features(self):
        columns = list(self.dataframe.columns.values)
        features = self.dataframe[['rain', 'precipi', 'Hour', 'meantempi']]
        return features

    def __compute_cost(self, features, values, theta):
        m = len(values)
        sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
        cost = sum_of_square_errors / (2 * m)
        return cost

    def __gradient_descent(self, features, values, theta, alpha, num_iterations):
        """
        Perform gradient descent given a data set with an arbitrary number of features.

        This can be the same gradient descent code as in the lesson #3 exercises,
        but feel free to implement your own.
        """

        m = len(values)
        cost_history = []

        for i in range(num_iterations):
            theta = theta - (alpha / len(values)) * np.dot(np.dot(features, theta) - values, features)
            cost = self.__compute_cost(features, values, theta)
            cost_history.append(cost)
        return theta, pandas.Series(cost_history)

    def compile_models(self):
        # Add UNIT to features using dummy variables
        dummy_units = pandas.get_dummies(self.dataframe['UNIT'], prefix='unit')
        features = self.features.join(dummy_units)

        # Values
        m = len(self.values)

        features, mu, sigma = normalize_features(features)
        features['ones'] = np.ones(m)  # Add a column of 1s (y intercept)

        # Convert features and values to numpy arrays
        features_array = np.array(features)
        values_array = np.array(self.values)

        # Set values for alpha, number of iterations.
        alpha = 0.1  # please feel free to change this value
        num_iterations = 75  # please feel free to change this value

        # Initialize theta, perform gradient descent
        theta_gradient_descent = np.zeros(len(features.columns))
        theta_gradient_descent, cost_history = self.__gradient_descent(features_array,
                                                                       values_array,
                                                                       theta_gradient_descent,
                                                                       alpha,
                                                                       num_iterations)
        # plot = plot_cost_history(alpha, cost_history)
        predictions = np.dot(features_array, theta_gradient_descent)
        return predictions


class OLSPredictModel(PredictModel):
    def compile_models(self):
        dummy_units = pandas.get_dummies(self.dataframe['UNIT'], prefix='unit')
        features = self.features.join(dummy_units)
        X = features
        y = np.array(self.values)
        X = sm.add_constant(X)
        olsmod = sm.OLS(y, X)
        olsres = olsmod.fit()
        ynewpred = olsres.predict(X)
        # print(olsres.summary())
        intercept , params = olsres.params[0],olsres.params[1:]
        print("intercept  =  %s"%intercept)
        return ynewpred


def normalize_features(df):
    mu = df.mean()
    sigma = df.std()

    if (sigma == 0).any():
        raise Exception("One or more features had the same value for all samples, and thus could " + \
                        "not be normalized. Please do not include features with only a single value " + \
                        "in your model.")
    df_normalized = (df - df.mean()) / df.std()
    return df_normalized, mu, sigma


def plot_cost_history(alpha, cost_history):
    cost_df = pandas.DataFrame({
        'Cost_History': cost_history,
        'Iteration': range(len(cost_history))
    })
    return ggplot(cost_df, aes('Iteration', 'Cost_History')) + \
           geom_point() + ggtitle('Cost History for alpha = %.3f' % alpha)


def plot_residuals(turnstile_weather, predictions):
    plt.figure()
    df = (turnstile_weather['ENTRIESn_hourly'] - predictions)
    df.hist()

    df.plot(kind='scatter', y='ENTRIESn_hourly')
    return plt


def r_squared(data, predictions):
    SSReg = ((predictions - data) ** 2).sum()
    SST = ((data - np.mean(data)) ** 2).sum()
    print SSReg
    print SST
    r_squared = 1 - SSReg / SST
    return r_squared


def predictions(weather_turnstile):
    #
    # Your implementation goes here. Feel free to write additional
    # helper functions
    #
    predictModel = PredictModel(weather_turnstile)
    # predictModel = OLSPredictModel(weather_turnstile)
    predictions = predictModel.compile_models()
    return predictions


current_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(current_path, 'turnstile_data_master_with_weather.csv')
turnstile_weather = pandas.read_csv(filename)

predictions_data = predictions(turnstile_weather)
print predictions_data
print "r^2 = %s" % r_squared(turnstile_weather["ENTRIESn_hourly"], predictions_data)
# r^2 = 0.458044314039 linear
# r^2 = 0.458044464741 OLS
# r^2 = 0.458044464741 OLS const
#http://statsmodels.sourceforge.net/devel/examples/