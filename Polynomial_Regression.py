from sklearn.datasets import load_diabetes
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np


X = np.random.rand(100,1)*4
y = 2+ 3*X**2 + np.random.rand(100,1)

poly _