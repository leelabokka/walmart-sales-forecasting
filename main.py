# Walmart Sales Forecasting using Machine Learning

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load dataset
data = pd.read_csv("Walmart.csv")

# Display first rows
print("First 5 rows of dataset:")
print(data.head())

# Fix date format (DD-MM-YYYY)
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)

# Create time features
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['Week'] = data['Date'].dt.isocalendar().week.astype(int)

# Features and target
X = data[['Store','Holiday_Flag','Temperature','Fuel_Price','CPI','Unemployment','Year','Month','Week']]
y = data['Weekly_Sales']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, predictions)
print("\nMean Squared Error:", mse)
rmse = np.sqrt(mse)
print("Root Mean Squared Error:", rmse)
r2 = r2_score(y_test, predictions)
print("R2 Score:", r2)
# Plot
plt.figure()
plt.scatter(y_test, predictions)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Walmart Sales")
plt.show()
