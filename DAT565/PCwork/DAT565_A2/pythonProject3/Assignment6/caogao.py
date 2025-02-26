import os

# 定义数据集路径
data_dir = r"D:\A6\mnist"

# 检查文件大小和格式
images_file = os.path.join(data_dir, "mnist_train")
file_size = os.path.getsize(images_file)
print(f"File size: {file_size} bytes")

# 检查是否是标准的 28x28 图像大小
expected_size = 28 * 28 * 60000  # 假设有 60000 张图像
print(f"Expected size: {expected_size} bytes")
