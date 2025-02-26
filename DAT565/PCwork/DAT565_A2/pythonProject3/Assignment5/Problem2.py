import os
os.environ["OMP_NUM_THREADS"] = "1"
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

file_path = r"D:\A5\normalized_seeds_with_labels.csv"
data = pd.read_csv(file_path)
features = data.iloc[:, :-1]
inertia = []
k_values = range(1, 11)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(features)
    inertia.append(kmeans.inertia_)
plt.figure(figsize=(8, 6))
plt.plot(k_values, inertia, marker='o')
plt.title('Inertia vs Number of Clusters (k)', fontsize=14)
plt.xlabel('Number of Clusters (k)', fontsize=12)
plt.ylabel('Inertia', fontsize=12)
plt.xticks(k_values)
plt.grid()
plt.show()
