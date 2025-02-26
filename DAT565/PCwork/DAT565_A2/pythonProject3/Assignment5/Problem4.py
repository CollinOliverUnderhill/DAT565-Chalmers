import os
os.environ["OMP_NUM_THREADS"] = "1"
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from scipy.optimize import linear_sum_assignment
import numpy as np

file_path = r"D:\A5\normalized_seeds_with_labels.csv"
data = pd.read_csv(file_path)
features = data.iloc[:, :-1]
true_labels = data.iloc[:, -1]
k = len(true_labels.unique())
kmeans = KMeans(n_clusters=k, random_state=42)
predicted_labels = kmeans.fit_predict(features)
rand_index = adjusted_rand_score(true_labels, predicted_labels)
print(f"Rand Index: {rand_index:.4f}")
confusion_matrix = np.zeros((k, k), dtype=int)
for true, pred in zip(true_labels, predicted_labels):
    confusion_matrix[true - 1, pred] += 1
row_ind, col_ind = linear_sum_assignment(-confusion_matrix)
accuracy = confusion_matrix[row_ind, col_ind].sum() / confusion_matrix.sum()
print(f"Clustering Accuracy: {accuracy:.4f}")
