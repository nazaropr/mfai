import random
from scipy.spatial.distance import euclidean
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def generate_data(n):
    return [[random.uniform(0, 1), random.uniform(0, 1)] for i in range(n)]


def distance_measure(x1, x2):
    return euclidean(x1, x2)


def k_means_clustering(X, k):
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(X)
    return kmeans.labels_


def hierarchical_clustering(X, k):
    Z = linkage(pdist(X), 'ward')
    labels = fcluster(Z, k, criterion='maxclust')
    return labels, Z


def plot_clusters(X, labels_kmeans, labels_hierarchical):
    fig, axs = plt.subplots(1, 2)

    # K-means clustering
    axs[0].scatter([x[0] for x in X], [x[1] for x in X], c=labels_kmeans)
    axs[0].set_title('K-means clustering')

    # Hierarchical clustering
    axs[1].scatter([x[0] for x in X], [x[1] for x in X], c=labels_hierarchical)
    axs[1].set_title('Hierarchical clustering')

    plt.show()


def compare_cluster_results(X, labels_kmeans, labels_hierarchical, Z):
    # K-means clustering
    kmeans_clusters = [[] for _ in range(len(set(labels_kmeans)))]
    for i in range(len(X)):
        kmeans_clusters[labels_kmeans[i]].append(X[i])

    # Hierarchical clustering
    hierarchical_clusters = [[] for _ in range(len(set(labels_hierarchical)))]
    for i in range(len(X)):
        hierarchical_clusters[labels_hierarchical[i] - 1].append(X[i])

    # Print number of points in each cluster and coordinates of cluster centers
    print('K-means clustering:')
    for i in range(len(kmeans_clusters)):
        print(f'Cluster {i}: {len(kmeans_clusters[i])} points ({np.mean(kmeans_clusters[i], axis=0)[0]:.5f}, {np.mean(kmeans_clusters[i], axis=0)[1]:.5f})')
    print('\nHierarchical clustering:')
    for i in range(len(hierarchical_clusters)):
        print(f'Cluster {i}: {len(hierarchical_clusters[i])} points ({np.mean(hierarchical_clusters[i], axis=0)[0]:.5f}, {np.mean(hierarchical_clusters[i], axis=0)[1]:.5f})')



if __name__ == '__main__':
    N = 1000
    X = generate_data(N)
    k = 5

    # K-means clustering
    labels_kmeans = k_means_clustering(X, k)

    # Hierarchical clustering
    labels_hierarchical, Z = hierarchical_clustering(X, k)

    plot_clusters(X, labels_kmeans, labels_hierarchical)

    compare_cluster_results(X, labels_kmeans, labels_hierarchical, Z)
