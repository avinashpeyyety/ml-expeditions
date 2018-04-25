#Understanding SVM
Support Vector Machines (SVMs) separates data points based on decision planes, which separates objects belonging to different classes in a higher dimensional space. SVM algorithm uses the best suitable kernel, which is capable of separating data points into two or more classes.

#Commonly used kernels are:
linear
polynomial
rbf
sigmoid

#Support Vector Classification
scikit-learn provides the following three utilities for performing Support Vector Classification.
SVC
NuSVC: Same as SVC but uses a parameter to control the number of support vectors.
LinearSVC: Similar to SVC with parameter kernel taking linear value.
  
#Support Vector Regression
scikit-learn provides the following three utilities for performing Support Vector Regression.
SVR
NuSVR
LinearSVR

#Advantages of SVMs
SVM can distinguish the classes in a higher dimensional space.
SVM algorithms are memory efficient.
SVMs are versatile, and a different kernel can be used by a decision function.

#Disadvantages of SVMs
SVMs do not perform well on high dimensional data with many samples.
SVMs work better only with Preprocessed data.
They are harder to visualize.

#Demo of Support Vector Classification
An example of creating an SVM classifier is shown below.
The shown model overfits the training data.
from sklearn.svm import SVC
svm_classifier = SVC()
svm_classifier = svm_classifier.fit(X_train, Y_train) 
print('Accuracy of Train Data :', svm_classifier.score(X_train,Y_train))
print('Accuracy of Test Data :', svm_classifier.score(X_test,Y_test))

#Improving Accuracy Using Scaled Data
In the following example, scaled input data is used to improve the accuracy of SVM classifier.
import sklearn.preprocessing as preprocessing
standardizer = preprocessing.StandardScaler()
standardizer = standardizer.fit(cancer.data)
cancer_standardized = standardizer.transform(cancer.data)
svm_classifier = SVC()
svm_classifier = svm_classifier.fit(X_train, Y_train) 

#Determining Accuracy of New Model
print('Accuracy of Train Data :', svm_classifier.score(X_train,Y_train))
print('Accuracy of Test Data :', svm_classifier.score(X_test,Y_test))

#Viewing the Classification Report
from sklearn import metrics
Y_pred = svm_classifier.predict(X_test)
print('Classification report : \n',metrics.classification_report(Y_test, Y_pred))
