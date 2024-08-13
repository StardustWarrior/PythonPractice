#Github for SKLearn: https://github.com/scikit-learn/sklearn-pypi-package

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import joblib

# Example data: Size of the house (square feet) and corresponding prices
X = np.array([[1000], [1500], [2000], [2500], [3000]])  # Size of the house
y = np.array([300000, 400000, 500000, 600000, 700000])  # Price of the house

# Create and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Generate predictions for the input data
predicted_prices = model.predict(X)

# Save the model to a file
joblib.dump(model, 'linear_regression_model.pkl')

# Plotting the data points and the regression line
plt.scatter(X, y, color='blue', label='Actual Prices')  # Actual data points
plt.plot(X, predicted_prices, color='red', label='Regression Line')  # Regression line
plt.xlabel('Size (sq ft)')
plt.ylabel('Price ($)')
plt.title('Linear Regression: House Prices vs. Size')
plt.legend()
plt.show()