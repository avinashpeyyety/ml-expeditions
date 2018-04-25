# Sample end to end Supervised Learning model execution: California Housing Dataset
# I. Raw Data Visualization and Analysis
import sklearn.preprocessing as preprocessing
import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt

dataset = fetch_california_housing()
print(dataset.DESCR)
dataset_np = np.c_[dataset['data'], dataset['target']]

# III. Splitting Data to Test & Train set :
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data[train_indices], data[test_indices]

train_set, test_set = split_train_test(dataset_np, 0.2)
print(len(train_set), "train +", len(test_set), "test")

xtrain = train_set[:,:8]
ytrain = train_set[:,8]
xtest = test_set[:,:8]
ytest = test_set[:,8]

print('xtrain: ',xtrain.shape,'\n')
print('xtest: ',xtest.shape,'\n')
print('ytrain: ',ytrain.shape,'\n')
print('ytest: ',ytest.shape)

df = pd.DataFrame(data = np.c_[xtrain, ytrain],
                  index=list(range(0,16512,1)),
                  columns=['average_income', 'housing_average_age', 'average_rooms', 'average_bedrooms', 'population',
                           'average_occupation', 'latitude', 'longitude','average_house_value'])
print(df)
df.plot(kind="scatter",
        x="longitude",
        y="latitude",
        alpha=0.5,
        s=df["population"]/100,
        label="population",
        c="average_house_value",
        cmap=plt.get_cmap("jet"),
        colorbar=True)
plt.legend()
plt.show()
plt.close()

# IV. Select and Train a Model: Training and Evaluating on the Training Set
# Running a linear regression model
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(xtrain, ytrain)

# Testing Regression model with RMSE to check if the model underfits or overfits
dataset_predictions = lin_reg.predict(xtest)
lin_mse = mean_squared_error(ytest, dataset_predictions)
lin_rmse = np.sqrt(lin_mse)
print(lin_rmse)

# Running a Decision tree model
from sklearn.tree import DecisionTreeRegressor
tree_reg = DecisionTreeRegressor()
tree_reg.fit(xtrain, ytrain)

# Testing Decision Tree model with RMSE to check if the model underfits or overfits
dataset_predictions = tree_reg.predict(xtest)
tree_mse = mean_squared_error(ytest, dataset_predictions)
tree_rmse = np.sqrt(tree_mse)
print(tree_rmse)

# Running a Random Forest model
from sklearn.ensemble import RandomForestRegressor
forest_reg = RandomForestRegressor()
forest_reg.fit(xtrain, ytrain)

# Testing Decision Tree model with RMSE to check if the model underfits or overfits
dataset_predictions = forest_reg.predict(xtest)
ypred = dataset_predictions
forest_mse = mean_squared_error(ytest, dataset_predictions)
forest_rmse = np.sqrt(forest_mse)
print(forest_rmse)

# Plot the Actuals and predictions for test Set using the predictions of the best model
df1 = pd.DataFrame(data = np.c_[xtest, ytest],
                  index=list(range(0,4128,1)),
                  columns=['average_income', 'housing_average_age', 'average_rooms', 'average_bedrooms', 'population',
                           'average_occupation', 'latitude', 'longitude','average_house_value'])
df1.plot(kind="scatter",
        x="longitude",
        y="latitude",
        alpha=0.5,
        s=df["population"]/100,
        label="population",
        c="average_house_value",
        cmap=plt.get_cmap("jet"),
        colorbar=True)
plt.legend()
plt.show()
plt.close()

df2 = pd.DataFrame(data = np.c_[xtest, ypred] ,
                  index=list(range(0,4128,1)),
                  columns=['average_income', 'housing_average_age', 'average_rooms', 'average_bedrooms', 'population',
                           'average_occupation', 'latitude', 'longitude','average_house_value'])
df2.plot(kind="scatter",
        x="longitude",
        y="latitude",
        alpha=0.5,
        s=df["population"]/100,
        label="population",
        c="average_house_value",
        cmap=plt.get_cmap("jet"),
        colorbar=True)
plt.legend()
plt.show()
plt.close()

'''
# V. Better Evaluation Using Cross-Validation
# Firstly define a utility function
from sklearn.model_selection import cross_val_score
def display_scores(scores):
    print("Scores:", scores)
    print("Mean:", scores.mean())
    print("Standard deviation:", scores.std())

tree_scores = cross_val_score(tree_reg,
                              dataset['data'],
                              dataset['target'],
                              scoring="neg_mean_squared_error",
                              cv=10)
tree_rmse_scores = np.sqrt(-tree_scores)
display_scores(tree_rmse_scores)

lin_scores = cross_val_score(lin_reg,
                             dataset['data'],
                             dataset['target'],
                             scoring="neg_mean_squared_error",
                             cv=10)
lin_rmse_scores = np.sqrt(-lin_scores)
display_scores(lin_rmse_scores)

forest_scores = cross_val_score(forest_reg,
                                dataset['data'],
                                dataset['target'],
                                scoring="neg_mean_squared_error",
                                cv=10)
forest_rmse_scores = np.sqrt(-forest_scores)
display_scores(forest_rmse_scores)
'''
