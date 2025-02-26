import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SequentialFeatureSelector

train_data = pd.read_csv(r'D:\TME202\train_life_expectancy.csv')
test_data = pd.read_csv(r'D:\TME202\test_life_expectancy.csv')
target_variable = 'Life Expectancy at Birth, both sexes (years)'
numeric_train_data = train_data.select_dtypes(include=[np.number]).drop(columns=[target_variable])
numeric_test_data = test_data.select_dtypes(include=[np.number]).drop(columns=[target_variable])
imputer = SimpleImputer(strategy='mean')
numeric_train_data = pd.DataFrame(imputer.fit_transform(numeric_train_data), columns=numeric_train_data.columns)
numeric_test_data = pd.DataFrame(imputer.transform(numeric_test_data), columns=numeric_test_data.columns)
y_train = train_data[target_variable]
y_test = test_data[target_variable]
model = LinearRegression()
sfs = SequentialFeatureSelector(model, n_features_to_select=3, direction='forward')
sfs.fit(numeric_train_data, y_train)
selected_features = numeric_train_data.columns[sfs.get_support()]
print(f'Selected features: {selected_features}')
X_train_selected = numeric_train_data[selected_features]
X_test_selected = numeric_test_data[selected_features]
model.fit(X_train_selected, y_train)
y_pred = model.predict(X_test_selected)
test_score = model.score(X_test_selected, y_test)
mse = mean_squared_error(y_test, y_pred)
correlation = np.corrcoef(y_pred, y_test)[0, 1]
print(f'Coefficient of determination (R^2) for test set: {test_score}')
print(f'Correlation between predictions and target: {correlation}')
print(f'Mean Squared Error (MSE): {mse}')

