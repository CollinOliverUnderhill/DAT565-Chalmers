import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.random_projection import GaussianRandomProjection
import umap.umap_ as umap


file_path = r"D:\A5\normalized_seeds_with_labels.csv"
data = pd.read_csv(file_path)
features = data.iloc[:, :-1]
labels = data.iloc[:, -1]
# a
sns.pairplot(
    pd.concat([features, labels.rename("ClassLabel")], axis=1),
    hue="ClassLabel",
    diag_kind="kde",
    palette="Set2"
)
plt.suptitle("Scatter Plot Matrix of Features Colored by Class Labels", y=1.02)
plt.show()
# b
grp = GaussianRandomProjection(n_components=2, random_state=42)
projected_data = grp.fit_transform(features)
projected_df = pd.DataFrame(projected_data, columns=["Component 1", "Component 2"])
projected_df["ClassLabel"] = labels
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Component 1", y="Component 2", hue="ClassLabel", data=projected_df, palette="Set2")
plt.title("Scatter Plot of Gaussian Random Projection", fontsize=14)
plt.xlabel("Component 1", fontsize=12)
plt.ylabel("Component 2", fontsize=12)
plt.legend(title="Class Label")
plt.grid()
plt.show()

# c
umap_reducer = umap.UMAP(n_components=2, random_state=42)
umap_data = umap_reducer.fit_transform(features)
umap_df = pd.DataFrame(umap_data, columns=["UMAP 1", "UMAP 2"])
umap_df["ClassLabel"] = labels
plt.figure(figsize=(8, 6))
sns.scatterplot(x="UMAP 1", y="UMAP 2", hue="ClassLabel", data=umap_df, palette="Set2")
plt.title("Scatter Plot of UMAP Projection", fontsize=14)
plt.xlabel("UMAP 1", fontsize=12)
plt.ylabel("UMAP 2", fontsize=12)
plt.legend(title="Class Label")
plt.grid()
plt.show()
