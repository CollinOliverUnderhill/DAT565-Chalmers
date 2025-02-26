import pandas as pd
import scipy.sparse
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

train_set = pd.read_csv('D:/program files/DATA3/train_set.csv')
test_set = pd.read_csv('D:/program files/DATA3/test_set.csv')
train_set = train_set[train_set['label'].isin(['easy_ham', 'spam'])]
test_set = test_set[test_set['label'].isin(['easy_ham', 'spam'])]
X_train_counts = scipy.sparse.load_npz('D:/program files/DATA3/X_train_counts.npz')
X_test_counts = scipy.sparse.load_npz('D:/program files/DATA3/X_test_counts.npz')
y_train = train_set['label']
y_test = test_set['label']
print(X_train_counts.shape)  # 打印特征矩阵的形状
print(y_train.shape)         # 打印标签的形状
