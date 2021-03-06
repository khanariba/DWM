#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 13:19:20 2019

@author: Shaikh Safiya Naaz Abdul Hakeem.
Topic:Implementation of Simple Linear regression. 
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset=pd.read_csv('Salary_Data.csv')     #imporing our dataset using pandas
x=dataset.iloc[:,:-1].values              #iloc[start:end for row,start:end for column] allrows 0 to -2 column(YOX)
y=dataset.iloc[:,1].values              #iloc[start:end for row,start:end for column] allrows 0 column(sALARY)

#SPLITTING THE DATASET INTO TRAINING AND TEST SETS
from sklearn.model_selection import train_test_split
#used model selection in place of cross_validation since the latter is deprecated

x_train, x_test, y_train, y_test= train_test_split(x,y,test_size=1/3,random_state=0)

#fitting simple linear regression to the training set

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)
#predicting the test set results
y_pred=regressor.predict(x_test)

#visualising the training set results
plt.scatter(x_train, y_train, color='red')
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('Salary vs Years Experiencee(Training set)')
plt.xlabel('Years of EXperience')
plt.ylabel('Salary')
plt.show()


#visualising the training set results
plt.scatter(x_test, y_test, color='red')
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('Salary vs Years Experiencee(Test set)')
plt.xlabel('Years of EXperience')
plt.ylabel('Salary')
plt.show()
 

