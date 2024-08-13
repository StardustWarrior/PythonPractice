import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.model_selection import train_test_split

# Prepare the data
# Feature matrix: Each row represents a house, and each column represents a feature (e.g., size, bedrooms, etc.)
house_features = np.array([
    [2100, 3, 2, 10, 8, 3, 1, 0, 2, 2, 1, 7, 9],
    [1600, 2, 1, 15, 6, 2, 1, 0, 1, 1, 0, 5, 7],
    [2400, 4, 3, 5, 9, 4, 1, 1, 3, 2, 1, 8, 10],
    [1400, 2, 1, 20, 5, 1, 0, 0, 1, 1, 0, 4, 6],
    [3000, 5, 4, 8, 10, 4, 1, 1, 3, 3, 1, 9, 10]
], dtype=np.float32)

# Target variable: House prices corresponding to each row of features
house_prices = np.array([750000, 450000, 850000, 350000, 950000], dtype=np.float32)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(house_features, house_prices, test_size=0.2, random_state=42)

# Normalize the features using the training data mean and standard deviation
features_mean = X_train.mean(axis=0)
features_std = X_train.std(axis=0)
X_train_normalized = (X_train - features_mean) / features_std
X_test_normalized = (X_test - features_mean) / features_std  # Use the same mean and std as the training data

# Normalize the target variable (house prices) using the training data mean and standard deviation
prices_mean = y_train.mean()
prices_std = y_train.std()
y_train_normalized = (y_train - prices_mean) / prices_std
y_test_normalized = (y_test - prices_mean) / prices_std  # Use the same mean and std as the training data

# Convert data to PyTorch tensors
X_train_tensor = torch.tensor(X_train_normalized)
y_train_tensor = torch.tensor(y_train_normalized).view(-1, 1)  # Reshape to be a column vector
X_test_tensor = torch.tensor(X_test_normalized)
y_test_tensor = torch.tensor(y_test_normalized).view(-1, 1)  # Reshape to be a column vector

# Define the Neural Network
class HousePriceNN(nn.Module):
    def __init__(self):
        super(HousePriceNN, self).__init__()
        self.fc1 = nn.Linear(13, 64)  # 13 input features, 64 neurons in the first hidden layer
        self.fc2 = nn.Linear(64, 32)  # 64 neurons to 32 in the second hidden layer
        self.fc3 = nn.Linear(32, 1)   # 32 neurons to 1 output (house price)

    def forward(self, x):
        x = torch.relu(self.fc1(x))  # Apply ReLU activation after the first layer
        x = torch.relu(self.fc2(x))  # Apply ReLU activation after the second layer
        x = self.fc3(x)              # No activation function for the output layer (linear output)
        return x

# Instantiate the model
model = HousePriceNN()

# Define Loss Function and Optimizer
loss_function = nn.MSELoss()  # Mean Squared Error loss
optimizer = optim.SGD(model.parameters(), lr=0.001)  # Stochastic Gradient Descent optimizer

# Train the Model
num_epochs = 1000
for epoch in range(num_epochs):
    model.train()  # Set the model to training mode
    optimizer.zero_grad()  # Zero the gradients for each batch
    predicted_prices = model(X_train_tensor)  # Forward pass: Compute predicted prices on training data
    loss = loss_function(predicted_prices, y_train_tensor)  # Compute the loss on training data
    loss.backward()  # Backward pass: Compute gradients
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)  # Gradient clipping
    optimizer.step()  # Update the model parameters

    # Print the loss every 100 epochs
    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

# Evaluate the Model on Test Data
model.eval()  # Set the model to evaluation mode
with torch.no_grad():  # Disable gradient computation for evaluation
    test_predictions = model(X_test_tensor)  # Predict prices for test data
    test_loss = loss_function(test_predictions, y_test_tensor)  # Compute the loss on test data
    test_predictions = test_predictions * prices_std + prices_mean  # Unnormalize the predictions
    y_test_unormalized = y_test_tensor * prices_std + prices_mean  # Unnormalize the actual test prices
    print(f"Test Loss: {test_loss.item():.4f}")
    print(f"Predicted prices on test data: {test_predictions.numpy().flatten()}")
    print(f"Actual prices on test data: {y_test_unormalized.numpy().flatten()}")

# Save the Model
torch.save(model.state_dict(), 'house_price_model.pth')