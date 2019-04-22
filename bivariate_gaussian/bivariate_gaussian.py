#!/usr/bin/python3

import numpy as np
import scipy.stats as stats
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 5, 5


def plot_bivariate_gaussian(mu_x, sigma_x, mu_y, sigma_y, cov):

    """ Create a filled countor plot of a bivariate Gaussian distribution."""

    # Define X and Y variables
    N = 100
    X = np.linspace(-5, 5, N)
    Y = np.linspace(-5, 5, N)
    X, Y = np.meshgrid(X, Y)

    # Mean vector and covariance matrix
    mu = np.array([mu_x, mu_y])
    sigma = np.array([[ sigma_x, cov], [cov,  sigma_y]])

    # Transform X and Y into 3-D array
    pos = np.empty(X.shape + (2,))
    pos[:, :, 0] = X
    pos[:, :, 1] = Y

    # Obtain bivariate Gaussian distribution
    F = multivariate_normal(mu, sigma)
    Z = F.pdf(pos)
    
    # Plot a filled contour
    fig, ax = plt.subplots()
    cs = ax.contourf(X, Y, Z, cmap=cm.viridis, levels=N)
    plt.savefig("bivariate_gaussian.png", dpi=300)
    plt.close()

plot_bivariate_gaussian(0, 1, 0, 1, 0)
