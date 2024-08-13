import numpy as np

# Input features for a house:
# [Size in square feet, Number of bedrooms, Number of bathrooms, Age of the house, 
# Location Quality, Condition, Garage, Pool, Flooring Type, Number of Floors, 
# Basement, Energy Efficiency Rating, Proximity to Amenities]
input_features = np.array([2100, 3, 2, 10, 8, 3, 1, 0, 2, 2, 1, 7, 9])

# Weights (model parameters):
# [Weight for Size, Weight for Bedrooms, Weight for Bathrooms, Weight for Age, 
# Weight for Location Quality, Weight for Condition, Weight for Garage, Weight for Pool, 
# Weight for Flooring Type, Weight for Number of Floors, 
# Weight for Basement, Weight for Energy Efficiency Rating, Weight for Proximity to Amenities]
weights = np.array([300, 500, 1000, -100, 2000, 1500, 5000, 10000, 2000, 3000, 1500, 2500, 3500])

# Perform matrix multiplication (dot product in this case) to predict the price
predicted_price = np.dot(input_features, weights)

# Actual price for comparison
actual_price = 750000

# Calculate Mean Squared Error (MSE)
# In this simple case, we'll treat this as a single data point, but normally you would calculate this over multiple examples
mse = np.mean((np.array([actual_price]) - np.array([predicted_price])) ** 2)

print(f"Predicted House Price: ${predicted_price}")
print(f"Actual House Price: ${actual_price}")
print(f"Mean Squared Error (MSE): {mse}")