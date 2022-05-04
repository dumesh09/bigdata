#import libraries
import matplotlib.pyplot as plt                                 #for plotting graph of x,y
import numpy as np                                             #for using data as array
from sklearn import linear_model                              #for model we want to predict by
import pandas as pd                                          #for loading csv file data to numpy array
from sklearn.metrics import mean_squared_error, r2_score     #for mean error and variance calculation
from sklearn.model_selection import train_test_split        #splitting training and testing sets

#load dataset
dataset=pd.read_csv("geography_industry.csv",encoding= 'unicode_escape')

#splitting to independent(x) and dependent(y) variables
x=dataset.iloc[:,2].values
y=dataset.iloc[:,3].values

#train and test data split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/3, random_state = 0)

#reshaping array to convert from 1D to 2D array
x_test=x_test.reshape(-1,1)
x_train=x_train.reshape(-1,1)

#"lin_reg" is our model calling model "LinearRegression()"
lin_reg=linear_model.LinearRegression()

#fitting our data in linear regression model
lin_reg.fit(x_train,y_train)

#making predictions
lin_reg_pred=lin_reg.predict(x_test)

#coef_ and intercept_ are coefficients and intercepts resp. for our model
print("Coefficients:\n",lin_reg.coef_)
print("Intercept:\n",lin_reg.intercept_)

# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(y_test, lin_reg_pred))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y_test, lin_reg_pred))

#Plotting the graph for test dataset
plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_test, lin_reg_pred, color = 'blue')
plt.title('Geography impact')
plt.xlabel('state')
plt.ylabel('industry')
plt.show()