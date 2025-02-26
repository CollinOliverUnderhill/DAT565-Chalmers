import os
import numpy as np

data_dir = r"D:\A6\mnist"
class CustomMNIST:
    def __init__(self, data_dir, train=True):
        images_file = os.path.join(data_dir, "mnist_train" if train else "mnist_test")
        labels_file = os.path.join(data_dir, "mnist_train_labels" if train else "mnist_test_labels")
        if not os.path.exists(images_file):
            raise FileNotFoundError(f"Image file not found: {images_file}")
        if not os.path.exists(labels_file):
            raise FileNotFoundError(f"Label file not found: {labels_file}")
        self.images = np.fromfile(images_file, dtype=np.uint8, offset=16).reshape(-1, 28, 28).astype(np.float32) / 255.0
        self.labels = np.fromfile(labels_file, dtype=np.uint8)
    def __len__(self):
        return len(self.labels)
    def __getitem__(self, idx):
        return self.images[idx], self.labels[idx]
train_dataset = CustomMNIST(data_dir, train=True)
test_dataset = CustomMNIST(data_dir, train=False)
print(f"Train dataset size: {len(train_dataset)}")
print(f"Test dataset size: {len(test_dataset)}")
