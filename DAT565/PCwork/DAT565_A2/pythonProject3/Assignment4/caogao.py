import pandas as pd

# Load the datasets
original_data = pd.read_csv('D:\\TME202\\life_expectancy.csv')
train_data = pd.read_csv('D:\\TME202\\train_life_expectancy.csv')
test_data = pd.read_csv('D:\\TME202\\test_life_expectancy.csv')

# Display column names of each dataset to help determine the correct target variable
print("Original dataset columns:")
print(original_data.columns)

print("\nTraining dataset columns:")
print(train_data.columns)

print("\nTesting dataset columns:")
print(test_data.columns)
