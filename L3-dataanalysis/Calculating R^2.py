import numpy as np
import pandas as pd
def f1(data, predictions):
    pre_dict = pd.Series(predictions,index = data.index)
    mw = data.mean()
    print np.square(data - pre_dict).sum()
    print np.square(data - mw).sum()
    r_squared = 1 - np.square(data - pre_dict).sum() / np.square(data - mw).sum()
    return r_squared

def f2(data, predictions):
    SSReg = ((predictions-data)**2).sum()
    SST = ((data-np.mean(data))**2).sum()
    print SSReg
    print SST
    r_squared = 1 - SSReg / SST
    return r_squared
    
def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE
    r_squared = f2(data, predictions)
    #r_squared = f1(data, predictions)
    
    return r_squared