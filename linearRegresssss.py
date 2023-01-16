import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class MyLinearRegression:

    def __init__(self):
        self.coef_ = None
        self.intercept_ = None
    
    def fit(self,x,y):
        x=np.array(x)
        y=np.array(y)[:,None]
        k0=np.ones_like(y)
        x=np.hstack((k0,x))
        weights = (np.linalg.inv(x.T @ x)) @ x.T @ y
        self.intercept_ = weights[0]
        self.coef_ = weights[1:].T

    def predict(self, x):
        x=np.array(x)
        return ((x @ self.coef_.T)+self.intercept_).T

model = MyLinearRegression()

data=pd.read_csv('penguins.csv')
x=data[data.columns[1:]]
y=data[data.columns[0]]
model.fit(x,y)

print(model.predict(x))