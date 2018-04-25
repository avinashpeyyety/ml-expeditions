#Introduction to Clustering
Clustering is one of the unsupervised learning technique.
The technique is typically used to group data points into clusters based on a specific algorithm.

#Major clustering algorithms that can be implemented using scikit-learn are:
K-means Clustering
Agglomerative clustering
DBSCAN clustering
Mean-shift clustering
Affinity propagation
Spectral clustering

#K-Means Clustering
In K-means Clustering entire data set is grouped into k clusters.
Steps involved are:
k centroids are chosen randomly.
The distance of each data point from k centroids is calculated. A data point is assigned to the nearest cluster.
Centroids of k clusters are recomputed.
The above steps are iterated till the number of data points a cluster reach convergence.
KMeans from sklearn.cluster can be used for K-means clustering.

#Agglomerative Hierarchical Clustering
Agglomerative Hierarchical Clustering is a bottom-up approach.
Steps involved are:
Each data point is treated as a single cluster at the beginning.
The distance between each cluster is computed, and the two nearest clusters are merged together.
The above step is iterated till a single cluster is formed.
AgglomerativeClustering from sklearn.cluster can be used for achieving this.
Merging of two clusters can be any of the following linkage type: ward, complete or average.
  
#Mean Shift Clustering
Mean Shift Clustering aims at discovering dense areas.
Steps Involved:
Identify blob areas with randomly guessed centroids.
Calculate the centroid of each blob area and shift to a new one, if there is a difference.
Repeat the above step till the centroids converge.
make_blobs from sklearn.cluster can be used to initialize the blob areas. MeanShift from sklearn.cluster can be used to perform Mean Shift clustering.

#Affinity Propagation
Affinity Propagation generates clusters by passing messages between pairs of data points, until convergence.
AffinityPropagation class from sklearn.cluster can be used.
The above class can be controlled with two major parameters:
preference: It controls the number of exemplars to be chosen by the algorithm.
damping: It controls numerical oscillations while updating messages.
  
#Spectral Clustering
Spectral Clustering is ideal to cluster data that is connected, and may not be in a compact space.
In general, the following steps are followed:
Build an affinity matrix of data points.
Embed data points in a lower dimensional space.
Use a clustering method like k-means to partition the points on lower dimensional space.
spectral_clustering from sklearn.cluster can be used for achieving this.

#Demo of KMeans:
An example of performing KMeans clustering is shown below
from sklearn.cluster import KMeans
kmeans_cluster = KMeans(n_clusters=2)
kmeans_cluster = kmeans_cluster.fit(X_train) 
kmeans_cluster.predict(X_test)

#Evaluating a Clustering algorithm
A clustering algorithm is majorly evaluated using the following scores:
Homogeneity: Evaluates if each cluster contains only members of a single class.
Completeness: All members of a given class are assigned to the same cluster.
V-measure: Harmonic mean of Homogeneity and Completeness.
Adjusted Rand index: Measures similarity of two assignments.
  
#Evaluation with scikit-learn
from sklearn import metrics
print(metrics.homogeneity_score(kmeans_cluster.predict(X_test), Y_test))
print(metrics.completeness_score(kmeans_cluster.predict(X_test), Y_test))
print(metrics.v_measure_score(kmeans_cluster.predict(X_test), Y_test))
print(metrics.adjusted_rand_score(kmeans_cluster.predict(X_test), Y_test))
