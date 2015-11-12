import numpy
import pandas

def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features 
    (input data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost
def predict(features,theta):
    return numpy.dot(features, theta)

def new_theta_cal(theta, alpha,features,values):
    feature_t = features.T
    negative_diff = ((values - predict(features, theta))*(feature_t))
    #print negative_diff
    negative_sum_diff = numpy.sum(negative_diff,axis = 1)
    #print negative_sum_diff
    theta_new = theta+(alpha/len(values))*negative_sum_diff
    return theta_new

def new_theta_cal2(theta, alpha,features,values):
    theta_new = theta-(alpha/len(values))*numpy.dot(predict(features, theta)-values, features)
    return theta_new
def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # Write code here that performs num_iterations updates to the elements of theta.
    # times. Every time you compute the cost for a given list of thetas, append it
    # to cost_history.
    # See the Instructor notes for hints.

    cost_history = []
    for time in range(0,1000):
        theta = new_theta_cal(theta, alpha,features,values)
        cost = compute_cost(features, values, theta)
        cost_history.append(cost)
    ###########################
    ### YOUR CODE GOES HERE ###
    ###########################

    return theta, pandas.Series(cost_history) # leave this line for the grader
