# Preprocessing - Preprocessing is a step, in which raw data is modified or transformed into a format, suitable for further downstream processing.
scikit-learn provides many preprocessing utilities such as:
Standardization mean removal
Scaling
Normalization
Binarization
One Hot Encoding
Label Encoding
Imputation
Correlation Plotting

# Standardization
Standardization or Mean Removal is the process of transforming each feature vector into a normal distribution with mean 0 and variance 1.
This can be achieved using StandardScaler. An example with its output is shown in the next two cards, which requires the following imports.
import sklearn.preprocessing as preprocessing
from sklearn.datasets import load_breast_cancer
dataset = load_breast_cancer()
standardizer = preprocessing.StandardScaler()
standardizer = standardizer.fit(dataset.data)
breast_cancer_standardized = standardizer.transform(dataset.data)
print('Mean of each feature after Standardization :\n\n')
print(breast_cancer_standardized.mean(axis=0))
print('\nStd. of each feature after Standardization :\n\n')
print(breast_cancer_standardized.std(axis=0))
print('\n\n')

# Scaling - Scaling transforms existing data values to lie between a minimum and maximum value.
MinMaxScaler transforms data to range 0 and 1.
MaxAbsScaler transforms data to range -1 and 1.
MinMaxScaler with specified range. In the below example, data is transformed to range 0 and 10.
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 10)).fit(dataset.data)
breast_cancer_minmaxscaled10 = min_max_scaler.transform(dataset.data)
print(breast_cancer_minmaxscaled10)
print('\n\n')

# Using MaxAbsScaler, the maximum absolute value of each feature is scaled to unit size, i.e., 1.
It is intended for data that is previously centered at sparse or zero data. By default, MaxAbsScaler transforms data to the range -1 and 1.
max_abs_scaler = preprocessing.MaxAbsScaler().fit(dataset.data)
breast_cancer_maxabsscaled = max_abs_scaler.transform(dataset.data)
print(breast_cancer_maxabsscaled)
print('\n\n')

# Using MinMaxScaler. #By default, transformation occurs to a range of 0 and 1. It can also be customized with feature_range argument as shown in next example.
min_max_scaler = preprocessing.MinMaxScaler().fit(dataset.data)
breast_cancer_minmaxscaled = min_max_scaler.transform(dataset.data)
print(breast_cancer_minmaxscaled)
print('\n\n')

# Normalization - Normalization scales each sample to have a unit norm. Normalization can be achieved with 'l1', 'l2', and 'max' norms.
'l1' norm makes the sum of absolute values of each row as 1, and 'l2' norm makes the sum of squares of each row as 1.
'l1' norm is insensitive to outliers. By default l2 norm is considered. Hence, removing outliers is recommended before applying l2 norm.
normalizer = preprocessing.Normalizer(norm='l1').fit(dataset.data)
breast_cancer_normalized = normalizer.transform(dataset.data)
In above example, l1 norm is used with norm parameter.

# Binarization - Binarization is the process of transforming data points to 0 or 1 based on a given threshold.
Any value above the threshold is transformed to 1, and any value below the threshold is transformed to 0. By default, a threshold of 0 is used.
binarizer = preprocessing.Binarizer(threshold=3.0).fit(dataset.data)
breast_cancer_binarized = binarizer.transform(dataset.data)
print(breast_cancer_binarized[:5,:5])

# OneHotEncoder - OneHotEncoder converts categorical integer values into one-hot vectors. In an on-hot vector, every category is transformed into a binary attribute having only 0 and 1 values.
An example creating two binary attributes for the categorical integers 1 and 2, is shown in the next slide.
onehotencoder = preprocessing.OneHotEncoder()
onehotencoder = onehotencoder.fit([[1], [1], [1], [2], [2], [1]])
Transforming category values 1 and 2 to one-hot vectors:
print(onehotencoder.transform([[1]]).toarray())
#print(onehotencoder.transform([[2]]).toarray())

# Imputation - Imputation replaces missing values with either median, mean, or the most common value of the column or row in which the missing values exist.
Below example replaces missing values, represented by np.nan, with the mean of respective column (axis 0).
imputer = preprocessing.Imputer(missing_values='NaN', strategy='mean')
imputer = imputer.fit(dataset.data)
breast_cancer_imputed = imputer.transform(dataset.data)

# Label Encoding - Label Encoding is a step in which, in which categorical features are represented as categorical integers. An example of transforming categorical valuelabels = [s ["benign","malignant"]into[0, 1]is shown below.
labels = ['malignant', 'benign', 'malignant', 'benign']
labelencoder = preprocessing.LabelEncoder()
labelencoder = labelencoder.fit(labels)
bc_labelencoded = labelencoder.transform(dataset.target_names)

# Correlation Plotting
