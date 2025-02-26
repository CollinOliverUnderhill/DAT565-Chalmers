import pandas as pd
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import scipy.sparse

train_set = pd.read_csv('D:/program files/DATA3/train_set.csv')
test_set = pd.read_csv('D:/program files/DATA3/test_set.csv')
train_set = train_set[train_set['label'].isin(['easy_ham', 'spam'])]
test_set = test_set[test_set['label'].isin(['easy_ham', 'spam'])]
X_train_counts = scipy.sparse.load_npz('D:/program files/DATA3/X_train_counts.npz')
X_test_counts = scipy.sparse.load_npz('D:/program files/DATA3/X_test_counts.npz')
X_train_counts = X_train_counts[train_set.index, :]
X_test_counts = X_test_counts[test_set.index, :]
y_train = train_set['label']
y_test = test_set['label']

multinomial_nb = MultinomialNB()
bernoulli_nb = BernoulliNB()
multinomial_nb.fit(X_train_counts, y_train)
y_pred_mnb = multinomial_nb.predict(X_test_counts)
accuracy_mnb = accuracy_score(y_test, y_pred_mnb)
precision_mnb = precision_score(y_test, y_pred_mnb, pos_label='spam', zero_division=1)
recall_mnb = recall_score(y_test, y_pred_mnb, pos_label='spam', zero_division=1)
confusion_mnb = confusion_matrix(y_test, y_pred_mnb)

print("Multinomial Naive Bayes Classifier Results:")
print(f"Accuracy: {accuracy_mnb:.4f}")
print(f"Precision: {precision_mnb:.4f}")
print(f"Recall: {recall_mnb:.4f}")
print("Confusion Matrix:")
print(confusion_mnb)

bernoulli_nb.fit(X_train_counts, y_train)
y_pred_bnb = bernoulli_nb.predict(X_test_counts)
accuracy_bnb = accuracy_score(y_test, y_pred_bnb)
precision_bnb = precision_score(y_test, y_pred_bnb, pos_label='spam', zero_division=1)
recall_bnb = recall_score(y_test, y_pred_bnb, pos_label='spam', zero_division=1)
confusion_bnb = confusion_matrix(y_test, y_pred_bnb)

print("\nBernoulli Naive Bayes Classifier Results:")
print(f"Accuracy: {accuracy_bnb:.4f}")
print(f"Precision: {precision_bnb:.4f}")
print(f"Recall: {recall_bnb:.4f}")
print("Confusion Matrix:")
print(confusion_bnb)
