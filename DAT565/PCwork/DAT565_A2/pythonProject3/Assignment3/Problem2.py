import pandas as pd
import scipy.sparse
from sklearn.feature_extraction.text import CountVectorizer

train_set = pd.read_csv('D:/program files/DATA3/train_set.csv')
test_set = pd.read_csv('D:/program files/DATA3/test_set.csv')
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(train_set['email'])
X_test_counts = vectorizer.transform(test_set['email'])
print(f"Training set shape: {X_train_counts.shape}")
print(f"Test set shape: {X_test_counts.shape}")
scipy.sparse.save_npz('D:/program files/DATA3/X_train_counts.npz', X_train_counts)
scipy.sparse.save_npz('D:/program files/DATA3/X_test_counts.npz', X_test_counts)

