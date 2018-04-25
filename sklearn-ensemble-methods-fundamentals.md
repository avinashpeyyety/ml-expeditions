# Ensemble Methods
Ensemble methods combine predictions of other learning algorithms, to improve the generalization.

# Ensemble methods are two types:
Averaging Methods: They build several base estimators independently and finally average their predictions.
E.g.: Bagging Methods, Forests of randomised trees
Boosting Methods: They build base estimators sequentially and trie to reduce the bias of the combined estimator.
E.g.: Adaboost, Gradient Tree Boosting
  
# Bagging Methods
Bagging Methods draw random subsets of the original dataset, build an estimator and aggregate individual results to form a final one.
BaggingClassifier and BaggingRegressor are the utilities from sklearn.ensemble to deal with Bagging.

# Randomized Trees
sklearn.ensemble offers two types of algorithms based on randomized trees: Random Forest and Extra randomness algorithms.
RandomForestClassifier and RandomForestRegressor classes are used to deal with random forests.
In random forests, each estimator is built from a sample drawn with replacement from the training set.
ExtraTreesClassifier and ExtraTreesRegressor classes are used to deal with extremely randomized forests.
In extremely randomized forests, more randomness is introduced, which further reduces the variance of the model.

# Boosting Methods:
Boosting Methods combine several weak models to create a improvised ensemble.
sklearn.ensemble also provides the following boosting algorithms:
AdaBoostClassifier
GradientBoostingClassifier

# Demo of Random Forest Classifier:
Example of creating a Random forest model is shown below.
from sklearn.ensemble import RandomForestClassifier
rf_classifier = RandomForestClassifier()
rf_classifier = rf_classifier.fit(X_train, Y_train) 
print('Accuracy of Train Data :', rf_classifier.score(X_train,Y_train))
print('Accuracy of Test Data :', rf_classifier.score(X_test,Y_test))
