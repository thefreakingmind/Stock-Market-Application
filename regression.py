#Regression for Stock Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import quandl as q
import math
from sklearn import *
from sklearn.linear_model import LinearRegression


# Google Dataset for Test
df = q.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. Close', 'Adj. High', 'Adj. Low', 'Adj. Volume']]
df['HLT'] = df['Adj. Open'] - df['Adj. Close']/df['Adj. Close'] * 100
df['PCT_CHANGE'] = df['Adj. High'] - df['Adj. Low']/df['Adj. Low'] * 100
forcast_column = 'Adj. Close'
df.fillna(-9999, inplace=True)
forcast_out = int(math.ceil(0.1*(len(df))))
df['label'] = df[forcast_column].shift(-forcast_out)
df.dropna(inplace=True)
print(df)
plt.plot(df)
plt.show()

x = np.array(df.drop(['label'],1))
y = np.array(df['label'])
x = preprocessing.scale(x)
df.dropna(inplace=True)
y = np.array(df['label'])

print(len(x))
print(len(y))
