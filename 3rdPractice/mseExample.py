import numpy as np

# Mean Squared Error (MSE)
actual = np.array([1, 2, 3])
predicted = np.array([1.1, 1.9, 3.2])
mse = np.mean((actual - predicted) ** 2)
print("Mean Squared Error:", mse)