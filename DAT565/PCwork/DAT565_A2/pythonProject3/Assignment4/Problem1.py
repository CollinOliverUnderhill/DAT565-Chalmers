import pandas as pd
from sklearn.model_selection import train_test_split

file_path = r'D:\TME202\life_expectancy.csv'
data = pd.read_csv(file_path)
print(data.info())
print(data.head())
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
print(f"Training set size: {train_data.shape}")
print(f"Test set size: {test_data.shape}")
train_data.to_csv(r'D:\TME202\train_life_expectancy.csv', index=False)
test_data.to_csv(r'D:\TME202\test_life_expectancy.csv', index=False)