import numpy as np
from scikit.cluster import Kmeans

def cluster(data_array, number_of_clusters):
    kmeans = KMeans(n_clusters=number_of_clusters).fit(np.array(data_array))
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_
    return labels, centers


def huge_cluster():
