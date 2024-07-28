import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import numpy as np


# -----------------------------------------Load datasets--------------------------------------------
classification_df = pd.read_csv(r'C:\Users\DELL\Desktop\BWT-ML-DL\WEEK-6\Classification\weather_classification_data.csv')
#There was a filenotfound error occuring when i just put the name of the weather data file in the path
# even though the file is in the same directory so i added the complete path


# Display the first few rows
print("Classification Dataset:")
print(classification_df.head())

# Identify missing values
print("\nMissing Values:")
print(classification_df.isnull().sum())

#------------------- ------------------------------Handle missing values-------------------------------------------------------
# Convert columns to appropriate data types
numeric_columns = ['Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)', 'Atmospheric Pressure', 'UV Index', 'Visibility (km)']
for column in numeric_columns:
    classification_df[column] = pd.to_numeric(classification_df[column], errors='coerce')

# Fill missing values with the mean for numeric columns
classification_df[numeric_columns] = classification_df[numeric_columns].fillna(classification_df[numeric_columns].mean())

# Fill missing values for categorical columns with mode
categorical_columns = ['Season', 'Location', 'Weather Type']
for column in categorical_columns:
    classification_df[column] = classification_df[column].fillna(classification_df[column].mode()[0])

# Convert categorical variables to numerical
label_encoder = LabelEncoder()
for column in categorical_columns:
    classification_df[column] = label_encoder.fit_transform(classification_df[column])

# Normalize/standardize numerical features
scaler = StandardScaler()
classification_df[numeric_columns] = scaler.fit_transform(classification_df[numeric_columns])

# Classification dataset
X_class = classification_df.drop('Weather Type', axis=1)
y_class = classification_df['Weather Type']
X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X_class, y_class, test_size=0.2, random_state=42)



# Print summary statistics

#---------------------------------------------------EDA-------------------------------------------------------------------------------
print("\nClassification Dataset Summary Statistics:")
print(classification_df.describe())

# -----------------------------------------Visualization--------------------------------------------------------------------------
# Histograms
classification_df.hist(figsize=(10, 10))
plt.suptitle('Classification Dataset - Histograms')
plt.show()

# Scatter plots
sns.pairplot(classification_df)
plt.suptitle('Classification Dataset - Scatter Plots')
plt.show()

# Box plots
plt.figure(figsize=(10, 6))
sns.boxplot(data=classification_df)
plt.title('Classification Dataset - Box Plots')
plt.show()

# Correlation heatmaps
plt.figure(figsize=(12, 8))
sns.heatmap(classification_df.corr(), annot=True, cmap='coolwarm')
plt.title('Classification Dataset - Correlation Heatmap')
plt.show()


#----------------------------------------------------classification model------------------------------------------------------

# Logistic Regression
lr_model = LogisticRegression()
lr_model.fit(X_train_class, y_train_class)
y_pred_lr = lr_model.predict(X_test_class)
print("Logistic Regression Classification Report:")
print(classification_report(y_test_class, y_pred_lr))

# Decision Tree
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train_class, y_train_class)
y_pred_dt = dt_model.predict(X_test_class)
print("Decision Tree Classification Report:")
print(classification_report(y_test_class, y_pred_dt))

# Random Forest
rf_model = RandomForestClassifier()
rf_model.fit(X_train_class, y_train_class)
y_pred_rf = rf_model.predict(X_test_class)
print("Random Forest Classification Report:")
print(classification_report(y_test_class, y_pred_rf))


#-----------------------------------------------model-performance comparison----------------------------------------------------------

# Performance metrics
models = ['Logistic Regression', 'Decision Tree', 'Random Forest']
metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
performance = {
    'Logistic Regression': classification_report(y_test_class, y_pred_lr, output_dict=True)['weighted avg'],
    'Decision Tree': classification_report(y_test_class, y_pred_dt, output_dict=True)['weighted avg'],
    'Random Forest': classification_report(y_test_class, y_pred_rf, output_dict=True)['weighted avg']
}

# Creating a performance DataFrame
performance_df = pd.DataFrame(performance).T[metrics]
print(performance_df)

# Visualize the performance
performance_df.plot(kind='bar', figsize=(10, 6))
plt.title('Model Performance Comparison')
plt.xlabel('Models')
plt.ylabel('Scores')
plt.legend(loc='best')
plt.show()


#just writing this line now on date 27 july to add  a ceratin commit message