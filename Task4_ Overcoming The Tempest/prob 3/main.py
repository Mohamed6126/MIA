import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
df=pd.read_csv('weatherHistory.csv')
sc=plt.scatter(x=df['Formatted Date'],y=df['Temperature (C)'])
plt.show()