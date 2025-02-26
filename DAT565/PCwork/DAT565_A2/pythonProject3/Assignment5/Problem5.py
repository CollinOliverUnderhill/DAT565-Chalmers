import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
from sklearn.metrics import accuracy_score
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt
import numpy as np

file_path = r"D:\A5\normalized_seeds_with_labels.csv"
data = pd.read_csv(file_path)
features = data.iloc[:, :-1]
true_labels = data.iloc[:, -1]
linkage_methods = ['single', 'complete', 'average', 'ward']
for method in linkage_methods:
    plt.figure(figsize=(10, 7))
    linked = linkage(features, method=method)
    dendrogram(linked, labels=true_labels.values, leaf_rotation=90, leaf_font_size=10)
    plt.title(f"Dendrogram ({method.capitalize()} Linkage)")
    plt.xlabel("Sample Index")
    plt.ylabel("Distance")
    plt.show()
linked = linkage(features, method='ward')
k = len(true_labels.unique())
predicted_labels = fcluster(linked, t=k, criterion='maxclust')
confusion_matrix = np.zeros((k, k), dtype=int)
for true, pred in zip(true_labels, predicted_labels):
    confusion_matrix[true - 1, pred - 1] += 1
row_ind, col_ind = linear_sum_assignment(-confusion_matrix)
accuracy = confusion_matrix[row_ind, col_ind].sum() / confusion_matrix.sum()
print(f"Clustering Accuracy (Ward Linkage): {accuracy:.4f}")
