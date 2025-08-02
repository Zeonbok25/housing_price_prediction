# LSTM Housing Price Prediction: Testing Guide

This guide explains how to test the LSTM-based housing price prediction model implemented in Python. The code analyzes spatial-temporal housing price data across different states, creates predictions, and evaluates model performance.

## System Requirements

Before running the code, ensure you have:
- Python 3.6 or higher
- Required Python packages: numpy, pandas, matplotlib, tensorflow, and scikit-learn

## Installation Instructions

1. Install the required packages using pip:
   ```
   pip install numpy pandas matplotlib tensorflow scikit-learn
   ```

2. Save the Python code in a file (e.g., `housing_lstm.py`)

3. Ensure your dataset (`price_coords_16y.csv`) is available at the specified path:
   ```
   D:/STDMcw/STDMcw/data/price_coords_16y.csv
   ```
   
## Running the Code

1. Execute the script from the command line or an IDE

2. The code will:
   - Load and preprocess the housing price data
   - Create LSTM models for the selected states (0, 13, 20)
   - Train the models and generate predictions
   - Display evaluation metrics (RMSE, MAE, MAPE, etc.)
   - Create visualizations of actual vs. predicted prices
   - Calculate overall performance metrics

3. The script also outputs:
   - Individual state performance metrics
   - Comparison of metrics across different states
   - Future price forecasts for the next 12 months
   - Growth rate analysis for each state

## Expected Outputs

- Console output of training progress and evaluation metrics
- Visualizations of the price predictions and error distributions
- Performance comparison across states
- Overall model performance metrics

## Data Processing Details

The code handles data processing through the `load_and_process_data()` function which:
- Reads the CSV file containing housing price data
- Filters out non-continental US regions (Hawaii, Alaska, etc.)
- Extracts the price matrix (starting from column 21)
- Handles missing values using forward-fill imputation

## Interpreting Results

After running the code, you'll receive:

1. **Individual model metrics** for each state showing:
   - MSE (Mean Squared Error)
   - RMSE (Root Mean Squared Error)
   - MAE (Mean Absolute Error)
   - R² (Coefficient of Determination)
   - MAPE (Mean Absolute Percentage Error)

2. **Visualizations** including:
   - Historical prices with training and test predictions
   - 12-month future forecasts
   - Error distribution histograms
   - Metric comparisons across states

3. **Growth rate analysis** showing:
   - Current prices
   - Predicted future prices
   - Percentage growth rates
   - Performance metrics for comparison

## Notes

- The code uses a fixed train/test split with 183 observations for training, which should be adjusted if your dataset differs in size.
- The LSTM model uses a lookback period of 6 months by default, which can be adjusted through the `look_back` parameter.
- Early stopping is implemented to prevent overfitting during training.
