


import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# -----------------------------------------Load datasets----------------------------------------------------------------------

regression_df = pd.read_csv(r'C:\Users\DELL\Desktop\BWT-ML-DL\WEEK-6\Regression\pakwheels_used_cars.csv')
#There was a filenotfound error occuring when i just put the name of the usedcars data file in the path
# even though the file is in the same directory so i added the complete path

# Display the first few rows and columns names
print("Regression Dataset:")
print(regression_df.head())
print("\nColumns in Regression Dataset:")
print(regression_df.columns)

# Identify missing values
print("\nMissing Values:")
print(regression_df.isnull().sum())

# Handle missing values
# Convert columns to appropriate data types
numeric_columns = ['engine_cc', 'mileage', 'price']
for column in numeric_columns:
    regression_df[column] = pd.to_numeric(regression_df[column], errors='coerce')

# Fill missing values with the mean for numeric columns
regression_df[numeric_columns] = regression_df[numeric_columns].fillna(regression_df[numeric_columns].mean())

# Update categorical columns based on actual dataset
categorical_columns = ['assembly', 'body', 'ad_city', 'color', 'fuel_type', 'make', 'model', 'registered', 'transmission']
for column in categorical_columns:
    if column in regression_df.columns:
        regression_df[column] = regression_df[column].fillna(regression_df[column].mode()[0])

# Convert categorical variables to numerical
label_encoder = LabelEncoder()
for column in categorical_columns:
    if column in regression_df.columns:
        regression_df[column] = label_encoder.fit_transform(regression_df[column])

# Normalize/standardize numerical features
scaler = StandardScaler()
regression_df[numeric_columns] = scaler.fit_transform(regression_df[numeric_columns])

# Prepare features and target variable
X_reg = regression_df.drop('price', axis=1, errors='ignore')
y_reg = regression_df['price']
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

# Print summary statistics
print("\nRegression Dataset Summary Statistics:")
print(regression_df.describe())

# -----------------------------------------Visualization--------------------------------------------
# Histograms
regression_df.hist(figsize=(10, 10))
plt.suptitle('Regression Dataset - Histograms')
plt.show()



# Box plots
plt.figure(figsize=(10, 6))
sns.boxplot(data=regression_df)
plt.title('Regression Dataset - Box Plots')
plt.show()

# Correlation heatmaps
plt.figure(figsize=(12, 8))
sns.heatmap(regression_df.corr(), annot=True, cmap='coolwarm')
plt.title('Regression Dataset - Correlation Heatmap')
plt.show()

# ----------------------------------------Regression Models-----------------------------------------
# Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train_reg, y_train_reg)
y_pred_lr = lr_model.predict(X_test_reg)
print("Linear Regression Performance:")
print(f"Mean Squared Error: {mean_squared_error(y_test_reg, y_pred_lr)}")
print(f"R^2 Score: {r2_score(y_test_reg, y_pred_lr)}")

# Decision Tree Regression
dt_model = DecisionTreeRegressor()
dt_model.fit(X_train_reg, y_train_reg)
y_pred_dt = dt_model.predict(X_test_reg)
print("\nDecision Tree Regression Performance:")
print(f"Mean Squared Error: {mean_squared_error(y_test_reg, y_pred_dt)}")
print(f"R^2 Score: {r2_score(y_test_reg, y_pred_dt)}")

# Random Forest Regression
rf_model = RandomForestRegressor()
rf_model.fit(X_train_reg, y_train_reg)
y_pred_rf = rf_model.predict(X_test_reg)
print("\nRandom Forest Regression Performance:")
print(f"Mean Squared Error: {mean_squared_error(y_test_reg, y_pred_rf)}")
print(f"R^2 Score: {r2_score(y_test_reg, y_pred_rf)}")

# -------------------------------------Model Performance Comparison--------------------------------------
# Performance metrics
models = ['Linear Regression', 'Decision Tree', 'Random Forest']
mse = [
    mean_squared_error(y_test_reg, y_pred_lr),
    mean_squared_error(y_test_reg, y_pred_dt),
    mean_squared_error(y_test_reg, y_pred_rf)
]
r2 = [
    r2_score(y_test_reg, y_pred_lr),
    r2_score(y_test_reg, y_pred_dt),
    r2_score(y_test_reg, y_pred_rf)
]

# Creating a performance DataFrame
performance_df = pd.DataFrame({
    'Mean Squared Error': mse,
    'R^2 Score': r2
}, index=models)
print("\nModel Performance:")
print(performance_df)

# Visualize the performance
performance_df.plot(kind='bar', figsize=(12, 6))
plt.title('Model Performance Comparison')
plt.xlabel('Models')
plt.ylabel('Scores')
plt.legend(loc='best')
plt.show()



#--------------------------------------------------Model Performance Comparison-------------------------------------------
#Based on the Mean Squared Error (MSE) and R² Score, the Random Forest Regression model performs the best in this scenario.
#Random Forest Regression has the lowest Mean Squared Error (0.494) and the highest R² Score (0.758), indicating that it predicts the car prices more accurately than the other models.
#Linear Regression performs moderately well, but not as good as Random Forest.
#Decision Tree Regression has the highest Mean Squared Error (1.107) and the lowest R² Score (0.448), making it the least accurate model among the three.

#Details I have written in the Report.

#Best Model: Random Forest Regression
          
