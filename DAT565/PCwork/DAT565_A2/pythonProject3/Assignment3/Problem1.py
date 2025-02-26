import tarfile
import os
import pandas as pd
import warnings
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore", category=DeprecationWarning)
def extract_tar_files(file_path, extract_path):
    with tarfile.open(file_path, 'r:bz2') as tar:
        tar.extractall(path=extract_path)
def load_emails_from_folder(folder_path):
    emails = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='latin1') as f:
                emails.append(f.read())
    return emails
easy_ham_path = 'D:/program files/DATA3/20021010_easy_ham.tar.bz2'
hard_ham_path = 'D:/program files/DATA3/20021010_hard_ham.tar.bz2'
spam_path = 'D:/program files/DATA3/20021010_spam.tar.bz2'
extract_dir = 'D:/program files/DATA3/Afterya'
os.makedirs(extract_dir, exist_ok=True)
extract_tar_files(easy_ham_path, extract_dir + '/easy_ham')
extract_tar_files(hard_ham_path, extract_dir + '/hard_ham')
extract_tar_files(spam_path, extract_dir + '/spam')
easy_ham_emails = load_emails_from_folder(extract_dir + '/easy_ham')
hard_ham_emails = load_emails_from_folder(extract_dir + '/hard_ham')
spam_emails = load_emails_from_folder(extract_dir + '/spam')
data = easy_ham_emails + hard_ham_emails + spam_emails
labels = ["easy_ham"] * len(easy_ham_emails) + ["hard_ham"] * len(hard_ham_emails) + ["spam"] * len(spam_emails)
df = pd.DataFrame({'email': data, 'label': labels})
# Train-test split
train_set, test_set = train_test_split(df, test_size=0.2, random_state=42, stratify=df['label'])
train_set.to_csv('D:/program files/DATA3/train_set.csv', index=False)
test_set.to_csv('D:/program files/DATA3/test_set.csv', index=False)
print(f"Training set size: {len(train_set)}")
print(f"Test set size: {len(test_set)}")
