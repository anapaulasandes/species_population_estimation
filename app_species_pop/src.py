import pandas as pd
import numpy as np
import pymc3 as pm
from scipy.stats import norm
import matplotlib.pyplot as plt


def estimate_params(data):
    with pm.Model() as model:
        mu = pm.Normal('mu', mu=0, sd=10)
        sigma = pm.HalfNormal('sigma', sd=10)
        
        # Define the likelihood of the data given the parameters
        y = pm.Normal('y', mu=mu, sd=sigma, observed=data)
        
        # Sample from the posterior distribution using MCMC
        trace = pm.sample(1000, chains=4)
        
    return trace

def plot_distribution(trace):
    # Plot the posterior distribution of the mean 
    pm.traceplot(trace, var_names=["mu"])
    plt.show()
