# Nearest Neighbors
Nearest neighbors method is used to determine a predefined number of data points that are closer to a sample point and predict its label.
sklearn.neighbors provides utilities for unsupervised and supervised neighbors-based learning methods.

# Nearest Neighbor Classifiers:
KNeighborsClassifier classifies based on k nearest neighbors of every query point, where k is an integer value specified by the user.
RadiusNeighborsClassifier classifies based on the number of neighbors present in a fixed radius r of every training point.

# Nearest Neighbors Regression:
KNeighborsRegressor predicts based on the k nearest neighbors of each query point.
RadiusNeighborsRegressor predicts based on the neighbors present in a fixed radius r of the query point.

# Demo of KNeighborsClassifier:
The following code snippet illustrates importing required modules and loading cancer dataset.
import sklearn.datasets as datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
cancer = datasets.load_breast_cancer()  # Loading the data set

# Building a Model of KNN classifier:
The following code creates training and test data sets, initializes a KNN classifier, and fits it with training data.
X_train, X_test, Y_train, Y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)
knn_classifier = KNeighborsClassifier()   
knn_classifier = knn_classifier.fit(X_train, Y_train) 

# Determining Accuracy of the Model:
The following code determines the accuracy of model on train and test data sets.
print('Accuracy of Train Data :', knn_classifier.score(X_train,Y_train))
print('Accuracy of Test Data :', knn_classifier.score(X_test,Y_test))
