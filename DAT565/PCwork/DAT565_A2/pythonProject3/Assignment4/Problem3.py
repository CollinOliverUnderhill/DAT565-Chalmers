import pandas as pd
import numpy as np
from scipy.stats import spearmanr
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

file_path = r'D:\TME202\life_expectancy.csv'
data = pd.read_csv(file_path)
train_data = pd.read_csv(r'D:\TME202\train_life_expectancy.csv')
target_variable = 'Life Expectancy at Birth, both sexes (years)'
numeric_train_data = train_data.select_dtypes(include=[np.number])
pearson_correlations = numeric_train_data.corrwith(train_data[target_variable])
spearman_correlations = numeric_train_data.apply(lambda col: spearmanr(col, train_data[target_variable])[0])
correlations_df = pd.DataFrame({
    'Variable': numeric_train_data.columns,
    'Pearson': pearson_correlations,
    'Spearman': spearman_correlations
}).dropna()
sorted_correlations = correlations_df.reindex(correlations_df['Spearman'].abs().sort_values(ascending=False).index)
print("Top variables with potential non-linear relationships:")
print(sorted_correlations.head())
candidate_variable = sorted_correlations.iloc[1]['Variable']
plt.scatter(train_data[candidate_variable], train_data[target_variable], color='blue', s=1)
plt.xlabel(candidate_variable)
plt.ylabel(target_variable)
plt.title(f'Relationship Between {candidate_variable} and Life Expectancy')
plt.show()
transformed_variable = np.log(train_data[candidate_variable] + 1)
original_pearson_corr = train_data[candidate_variable].corr(train_data[target_variable])
transformed_pearson_corr = pd.Series(transformed_variable).corr(train_data[target_variable])
print(f'Original Pearson correlation (before transformation): {original_pearson_corr}')
print(f'Pearson correlation (after transformation): {transformed_pearson_corr}')
plt.scatter(transformed_variable, train_data[target_variable], color='green', s=1)
plt.xlabel(f'Log-transformed {candidate_variable}')
plt.ylabel(target_variable)
plt.title(f'Transformed Relationship Between {candidate_variable} and Life Expectancy')
plt.show()
