import joblib

# Load the model from the file
loaded_model = joblib.load('linear_regression_model.pkl')

# Use the loaded model to make predictions
predicted_price = loaded_model.predict([[2200]])
print(f"Predicted price for a 2200 sq ft house: ${predicted_price[0]:.2f}")