#Regression Analysis

#Simple Linear Regression:
Consider the dataset provided.
X: 160 180 200 220 240 260 280
Y: 126 103  82 75  82 40 20
The first column provides the price of the house and the second column provides the number of houses sold. You want to fit a model where the price of a given house can predict the number of houses sold.
One way of predicting the number of houses sold is by using the arithmetic mean . This is the Base Model.
Irrespective of the price of a given house, the number of houses sold will be a **constant ** according to the model.
But does the mean describe the data well ?
In this model the line describes the data better than the mean.
Is this the best model?
If this is the best model why is it not passing through all the lines ?
So, what is the error ?
There is no straight line that can pass through all the points:
So ,how do you determine the best model ?
The best model is one that minimizes errors across all points . So you should take one line that minimizes the error across all the points.
In this diagram,
The actual values are scattered and the predicted values are along the line.
The difference between actual and predicted values gives the error. This is also called the residual error (e).
The parameters (Beta0 and Beta1) are chosen to minimize the total error between the actual and predicted values.

Measure of Quality:
You have seen how to fit a model that best describes the data. However, you can never get a perfect fit.
How will you measure the error/deviation in a model that is fit to the data ?

Sum of Squared Errors:
Sum of Squared Errors (SSE) is a measure of the quality of the Regression Line .
If there are n data points, then the SSE is the sum of square of the residual errors .
SSE is small for the Line of Best Fit and big for the baseline model.

Best Fit Line:
The line with the minimum SSE is the Regression Line. SSE is sometimes difficult to interpret because,
It depends on the number of values (n)
The units are hard to comprehend
So, is there a better way to gauge the quality of the Regression Model ?

RMSE:
At times, the SSE is difficult to interpret and the units are difficult to comprehend. So, the alternative measure of quality is the Root Mean Square Error (RMSE).
RMSE shrinks the magnitude of error by taking the square root of SSE divided by the number of observations (n).

Best Model vs Baseline Model:
The baseline model gives the Average value.
The SSE values for baseline model is the Total Sum of Square values(SST)
RSquare = 1 - ((SSE) / (SST))

R Square(R Sq) Properties:
SSE and SST values should be greater than zero.
R Sq lies between 0 and 1.
R Sq is a unit less quantity.
R Sq = 0 means the model is just as good as the base line and there is no improvement from the baseline model.
R Sq = 1 means it is a perfect model. Ideally, you should strive towards getting the R Sq close to 1 . But some models with R Sq = 0 are also accepted depending on the scenario.

Model Interpretation:
This is the equation for line of best fit
y = 249.85714 - 0.7928571x
For a unit change in X there is a .793 decrease in Y
For a unit increase in price of the house, .793 lesser houses are sold .
B0 is 249.85714
B1 is -0.7928571

#SLR using Python
Playground Setup - To setup the playground and try the code, install the following: -Go the terminal and enter the following command 
**pip install --user statsmodels **. If your installation is successful you should get the following message:
Installing collected packages: patsy, statsmodels
Successfully installed patsy-0.4.1 statsmodels-0.8.0

statsmodels is a complement to scipy package and provides the following :
Descriptive Statistics
Estimation and Inference for statistical Models

Data Frame Creation:
Let us now setup the initial data for our regression analysis. You will need to load Price and No of house units sold into the data frame.
import pandas as pd
price = [160,180,200,220,240,260,280]
sale = [126,103,82,75,82,40,20]
priceDF = pd.DataFrame(price, columns=list('x'))
saleDF = pd.DataFrame(sale, columns=list('y'))
houseDf = pd.concat((priceDF, saleDF),axis=1)
print(houseDf)
print(priceDF)

Statsmodels Usage:
Let us now see how to fit the data and get the regression outputs in Python.
Statsmodel can take input similar to R (Pass the variables with the dataframe) or take input as arrays.
Input as dataframe:
import statsmodels.api as sm
import statsmodels.formula.api as smf
smfModel = smf.ols('y~x',data=houseDf).fit()
print(smfModel.summary())

Understanding the Output:
Dep. Variable: The Dependent Variable
Model: Algorithm used. Here, it is Ordinary Least Squares
Method: Parameter Fitting method. Here, it is Least Squares
No. Observations: Number of rows used for model fitting.
DF Residuals: The degrees of freedom of the residuals (Difference between the number of observations and parameters).
DF Model: The degrees of freedom of the model (The number of parameters estimated in the model excluding the constant term) .
R-squared: Measure that says how well the model has performed with respect to the baseline model.
  
Data Prep:
Now that you understand how to perform regression analysis using statsmodel, it's time execute the data set created using the following code:
from sklearn.datasets import fetch_california_housing
from sklearn.datasets import load_boston
import pandas as pd 
boston = load_boston()
california = fetch_california_housing()
dataset = pd.DataFrame(boston.data, columns=boston.feature_names)
dataset['target'] = boston.target
print(dataset.head()) 

#Multi Linear Regression
Why Multiple Linear Regression ?
In the previous topics you have learnt how to predict one variable from another.
In this topic you will learn how to predict a variable using more than one variable.

MLR Representation
The MLR model is represented as,
y - Dependent variable
x - Independent variable
e - Error measure
B0 , B1 ,B2 … Bk Parameters that best fit the model

MLR - Multiple Regression helps in predicting a single variable using multiple independent variables. This improves the model by increasing the accuracy
In today's complex world a given phenomenon(variable) is affected by more than one variable. Hence it is advised to opt for a Multiple Regression Model

MLR Model Building:
Consider that for a given dependent variable y, there are 4 independent variables x1,x2,x3 and x4 that affect the outcome. A possible way of building a Multiple Regression Model is to first use each independent variable separately against the dependent variable and measure the R2 value.
Another way of doing this is by incrementally adding each dependent variable and measuring the R2 value for each combination.

MLR Model Example:
During this model fitting process, some variables will contribute significantly to the model but some might not. It is better to remove variables that are not of significance to the model. -So, how do we check if a variable is significant for the output? Let's take a look at that in the following cards.

Law of Diminishing Returns:
More variables can increase the accuracy of the model. But sometimes the incremental value of adding each new variable might decrease.
According to the Law of Diminishing Returns, the marginal improvement decreases as new variables are added.
For example,
When you include x1 and x2 variables the R Sq = .8
When you add x3 to the model the R Sq might become .85
Finally when you add x4 to this model the R Sq might become .87.
In this process the incremental value has reduced from .05 to .02

MLR Data:
Price(thousands of $) x
Sales of new homes y
Number of red cars z
Data Source : http://www.yale.edu/statlab
    
MLR Equation:
The MLR equation is, y = 252.85965 - .824935 x 1 + .3592748 x 2
The number of houses sold is a linear function of both the price of a house and number of cars sold
A unit increase in the number of cars sold increases the number of houses sold by a proportion of .35
A unit increase in price of a house decreases the number of houses sold by a proportion of .82
B0 252.85965
B1 -0.824935
B2 0.3592748
You will see the computation of B0,B1,B2 in the next set of cards.

What is Multi Collinearity ?
Multi collinearity happens when two independent variables in a Multiple Regression model are correlated to each other. This will affect the outcome of your regression model.
The best way to avoid multi collinearity is to omit one of the independent variables that is highly correlated with the other. The variable to omit depends on how the variable behaves in the presence of other variables.

Best Practices while Fitting MLR:
Determine the correlation matrix of all the independent variables .
Omit the terms that has high correlation with another.
Remove the terms that do not predict the output significantly.

#MLR using Python
Input Data Load:
Let us consider the dataset available in the previous topic.
Price of the House , Number of units sold and the number of cars sold.
Let us create a dataframe from the list using the following code.
import pandas as pd
price = [160,180,200,220,240,260,280]
sale = [126,103,82,75,82,40,20]
cars = [0,9,19,5,25,1,20]
priceDF = pd.DataFrame(price, columns=list('x'))
saleDF = pd.DataFrame(sale, columns=list('y'))
carsDf = pd.DataFrame(cars, columns=list('z'))
houseDf = pd.concat((priceDF,saleDF,carsDf),axis=1)

Fitting the Model:
Here we fit the model by giving the dependent (number of units sold) and independent variables (price of the house, number of cars sold).
X = houseDf.drop(['y'], axis=1)
y = houseDf.y
Xc = sm.add_constant(X)
linear regression = sm.OLS(y,Xc)
fitted_model = linear_regression.fit()
fitted_model.summary()

Interpreting the terms:
Coef column gives the value of estimated coefficients (B0, B1, B2 etc.) .
If the coef is zero then that independent variable does not predict the dependent variable correctly.
Std err denotes how much each coefficient varies from the estimated value
t-value - = Estimated coef/stderr
P(>|t|) how likely the estimated value is zero
This value also indicates how significant a variable is to a model.
The smaller the value, the more significant a given variable is to the model.
it is better to remove variables with higher values of P(>|t|)

Interpreting the Coef of the Model:
The final equation is y = 252.85965 - .824935 x 1 + .3592748 x 2
the P(>|t|) values for each parameter is
Constant Term 252.85965 is 0.001 - meaning - this term is significant in predicting the output
X - House Price - -0.8249 is 0.003 - this term is also significant in predicting the output. z - car sales - 0.3593 is 0.551 this term is not so significant in predicting the output.
We do not have to omit the third variable.

Handling Multicollinearity:
A good practice while fitting multiple regression model is to check if there is any correlation among the independent variables.
In python, for a random array X the command to find correlation is X.corr().

Quick Fact:
Choose the coef with low Pr(>|t|) value.
Reject one variable with correlation outside the range 0.7 and 0.7 with any other variable.

Data Prep:
Hope you've understood how to deal with multiple variables and perform multiple regressions. Let us consider the dataset created using the following code for further practice.
from sklearn.datasets import fetch_california_housing
from sklearn.datasets import load_boston
boston = load_boston()
california = fetch_california_housing()
dataset = pd.DataFrame(boston.data, columns=boston.feature_names)
dataset['target'] = boston.target
Hands On - From the previous card load all the variables other than target into a variable named X
Run a correlation among all independent variables to check for multi collinearity

#Model improvement Tips and Tricks
Occam's razor:
When you have two Multiple Regression Models fit for a given data set ,if one is simple and another is complex , choose the simple model.
Whenever you are in the Model Building exercise , start with a simple model and then build complexity on top of it.

Data Understanding:
Understanding data is the most important step before building a model. You should not apply regression for the sake of applying . After applying Regression, work to interpret the results and derive the appropriate insights required for further analysis.

Quick Fact:
Do not discard theoretical considerations based on statistical measures.

Feature Scaling:
Your data-set might contain different features like independent variables (columns) with different magnitudes. So always bring them to a proper scale for ease of operation. This process is called feature scaling.
You can achieve Feature scaling with the help of either Normalization or Standardization depending on the magnitude of the variables.

Normalization:
Normalization is the process of re-scaling any value to the range [-1,1] .
Python has ready-made packages for re-scaling the data
from sklearn import preprocessing
import numpy as np
sampleData = np.array([[ -3., -1.,  4.]])
normalized_sampleData = preprocessing.normalize(sampleData)
normalized_sampleData

Standardization:
Standardization is the process of removing the arithmetic mean and dividing by the standard deviation.
Standardization in python is done in the following way:
from sklearn.preprocessing import StandardScaler
X = np.array([1,2,3,4,5])
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
output : array([-1.41421356, -0.70710678,  0.        ,  0.70710678,  1.41421356])
