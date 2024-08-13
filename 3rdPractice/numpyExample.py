import numpy as np

# Input features for a house: [Size in square feet, Number of bedrooms, Age of the house]
input_features = np.array([2100, 3, 20])

# Weights (model parameters): [Weight for Size, Weight for Bedrooms, Weight for Age]
weights = np.array([700, 1000, -50])

# Perform matrix multiplication (dot product in this case)
predicted_price = np.dot(input_features, weights)

actual_price = 1500000

print(f"Predicted House Price: ${predicted_price}")
print(f"Actual House Price: ${actual_price}")