# %% [markdown]
# # 📝 Exercise 02
#
# The goal of this exercise is to build an intuition on what will be the
# parameters' values of a linear model when the link between the data and the
# target is non-linear.
#
# First, we will generate such non-linear data.
#
# ```{tip}
# `np.random.RandomState` allows to create a random number generator which can
# be later used to get deterministic results.
# ```

# %%
import numpy as np
# fix the seed for reproduction
rng = np.random.RandomState(0)

# generate data
n_sample = 100
x_max, x_min = 1.4, -1.4
len_x = (x_max - x_min)
x = rng.rand(n_sample) * len_x - len_x / 2
noise = rng.randn(n_sample) * .3
y = x ** 3 - 0.5 * x ** 2 + noise

# %%
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context("talk")

plt.scatter(x, y)
plt.xlabel('x')
_ = plt.ylabel('y')

# %% [markdown]
# We observe that the link between the data `x` and target `y` is non-linear.
# For instance, `x` could represent to be the years of experience (normalized)
# and `y` the salary (normalized). Therefore, the problem here would be to
# infer the salary given the years of experience.
#
# Using the function `f` defined below, find both the `weight` and the
# `intercept` that you think will lead to a good linear model. Plot both the
# data and the predictions of this model. Compute the mean squared error as
# well.


# %%
def f(x, weight=0, intercept=0):
    y_predict = weight * x + intercept
    return y_predict


# %%
# Write your code here.: plot both the data and the model predictions

# %%
# Write your code here.: compute the mean squared error

# %% [markdown]
# Train a linear regression model and plot both the data and the predictions
# of the model. Compute the mean squared error with this model.

# %%
from sklearn.linear_model import LinearRegression

# Write your code here.: fit a linear regression

# %%
# Write your code here.: plot the data and the prediction of the linear
# regression model

# %%
# Write your code here.: compute the mean squared error
