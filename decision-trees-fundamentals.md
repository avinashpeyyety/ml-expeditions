#Decision Trees

Decision Trees is another Supervised Learning method used for Classification and Regression. Decision Trees learn simple decision rules from training data and build a Model. DecisionTreeClassifier and DecisionTreeRegressor are the two utilities from sklearn.tree, which can be used for classification and regression respectively.

#Advantages of Decision Trees:

Decision Trees are easy to understand.
They often do not require any preprocessing.
Decision Trees can learn from both numerical and categorical data.

#Disadvantages of Decision Trees:

Decision trees sometimes become complex, which do not generalize well and leads to overfitting. Overfitting can be addressed by placing the least number of samples needed at a leaf node or placing the highest depth of the tree.
A small variation in data can result in a completely different tree. This problem can be addressed by using decision trees within an ensemble.

#Building a Decision Tree Classifier Model:

The subsequent code represents the building of a Decision Tree Classifier model.
Before executing this code, perform importing required modules, load cancer dataset, and create train and test data sets as shown in Neighbors classifier example.
from sklearn.tree import DecisionTreeClassifier
dt_classifier = DecisionTreeClassifier()   
dt_classifier = dt_classifier.fit(X_train, Y_train) 

#Determining Accuracy of the Model:

Further the below code determines the model accuracy. You can observe that the model is overfitted.
print('Accuracy of Train Data :', dt_classifier.score(X_train,Y_train))
print('Accuracy of Test Data :', dt_classifier.score(X_test,Y_test))

#Fine Tuning the Model:

Further the model is improved with change in max_depth value to 2.
dt_classifier = DecisionTreeClassifier(max_depth=2)   
dt_classifier = dt_classifier.fit(X_train, Y_train) 
print('Accuracy of Train Data :', dt_classifier.score(X_train,Y_train))
print('Accuracy of Test Data :', dt_classifier.score(X_test,Y_test))
