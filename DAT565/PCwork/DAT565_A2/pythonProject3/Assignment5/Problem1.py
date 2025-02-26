import pandas as pd
from sklearn.preprocessing import StandardScaler

file_path = r"D:\A5\seeds.tsv"
output_path = r"D:\A5\normalized_seeds_with_labels.csv"
data = pd.read_csv(file_path, sep="\t")
features = data.iloc[:, :-1]
labels = data.iloc[:, -1]
scaler = StandardScaler()
normalized_features = scaler.fit_transform(features)
normalized_data = pd.DataFrame(normalized_features, columns=features.columns)
normalized_data['ClassLabel'] = labels
normalized_data.to_csv(output_path, index=False)
print(f"Normalized data saved to: {output_path}")
