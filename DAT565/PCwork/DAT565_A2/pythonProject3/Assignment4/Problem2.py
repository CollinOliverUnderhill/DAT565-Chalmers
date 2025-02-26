import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

file_path = r'D:\TME202\life_expectancy.csv'
data = pd.read_csv(file_path)
train_data = pd.read_csv(r'D:\TME202\train_life_expectancy.csv')
test_data = pd.read_csv(r'D:\TME202\test_life_expectancy.csv')
# a)
target_variable = 'Life Expectancy at Birth, both sexes (years)'
numeric_train_data = train_data.select_dtypes(include=[np.number])
correlations = numeric_train_data.corr()
predictor_variable = correlations[target_variable].drop(target_variable).idxmax()
pearson_corr = train_data[predictor_variable].corr(train_data[target_variable])
print(f'Pearson correlation coefficient: {pearson_corr}')
# b)
X_train = train_data[[predictor_variable]]
y_train = train_data[target_variable]
model = LinearRegression()
model.fit(X_train, y_train)
print(f'Coefficient of determination: {model.score(X_train, y_train)}')
print(f'Model coefficients: {model.coef_[0]}')
print(f'Intercept: {model.intercept_}')
plt.scatter(X_train, y_train, color='blue', s=1)  # Adjusted 's' to make points smaller
plt.plot(X_train, model.predict(X_train), color='red')
plt.xlabel(predictor_variable)
plt.ylabel(target_variable)
plt.title('Linear Relationship Between Predictor and Life Expectancy')
plt.show()
# c)
X_test = test_data[[predictor_variable]]
y_test = test_data[target_variable]
y_pred = model.predict(X_test)
correlation = np.corrcoef(y_pred, y_test)[0, 1]
mse = mean_squared_error(y_test, y_pred)
print(f'Correlation between predictions and target: {correlation}')
print(f'Mean Squared Error: {mse}')


