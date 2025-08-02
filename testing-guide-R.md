# Instructions for Testing the Spatio-Temporal Housing Price Analysis Code

This document provides instructions for setting up and running the spatio-temporal analysis of U.S. housing prices. The analysis includes exploratory data analysis, autocorrelation analysis, and forecasting models.

## Prerequisites

### Software Requirements
- R (version 4.0.0 or higher recommended)
- RStudio (for easier workflow management)

### Required R Packages
The following packages need to be installed:

```r
# Core packages
install.packages(c("zoo", "reshape", "lattice", "ggplot2", "OpenStreetMap", "raster"))

# Spatial analysis packages
install.packages(c("sf", "spdep", "tmap"))

# Time series analysis packages
install.packages(c("forecast", "fpp2"))

# Deep learning packages (for LSTM model)
install.packages(c("keras", "tensorflow"))
```


## Data Setup

1. Create a directory structure as follows:
   ```
   D:/STDMcw/STDMcw/data/
   ```

2. Download and place the following datasets in the data directory:
   - `price_coords_16y.csv` - The main housing price dataset
   - `tl_2023_us_state/tl_2023_us_state.shp` - U.S. state shapefile (and associated files)

## Running the Analysis

### Step 1: Exploratory Data Analysis

1. Open RStudio and create a new R script
2. Copy the first section of the code (up to the "Spatial autocorrelation" section)
3. Run the code segment by segment to:
   - Load and preprocess the data
   - Generate basic statistical analysis
   - Create spatial and temporal visualizations
   - Produce heatmaps of the price patterns

### Step 2: Spatio-Temporal Autocorrelation Analysis

1. Make sure the spatial packages are installed
2. Run the autocorrelation analysis sections to:
   - Calculate and visualize temporal autocorrelation
   - Compute global and local Moran's I statistics
   - Generate LISA cluster maps

### Step 3: Time Series Forecasting with ARIMA/SARIMA

1. Run the time series analysis code to:
   - Decompose the time series
   - Test different ARIMA/SARIMA models
   - Evaluate forecasting performance
   - Visualize predictions

### Step 4: STARIMA Modeling

1. Run the STARIMA modeling code to:
   - Create spatial weight matrices
   - Analyze spatio-temporal autocorrelation
   - Fit the STARIMA model
   - Generate and evaluate spatio-temporal forecasts


## Troubleshooting

1. **Missing packages error**: Make sure all packages are installed correctly. Some may require system dependencies.
   
2. **File path errors**: Adjust the file paths in the code to match your directory structure if different from `D:/STDMcw/STDMcw/data/`.


3. **Memory issues**: When working with large datasets, increase R's memory allocation:
   ```r
   memory.limit(size=10000)  # Allocate 10GB of RAM
   ```

## Customization Options

- To analyze a different state or region, modify the filtering in the data preprocessing steps
- To adjust the forecast horizon, change the parameters in the prediction functions
- To tune model parameters, modify the `order` and `seasonal` arguments in the ARIMA/SARIMA models

## Output Verification

To verify that the code is working correctly:

1. Check that the spatial maps render properly with color-coded states
2. Ensure time series plots show clear trends and patterns
3. Verify that forecast plots include both actual and predicted values
4. Check that error metrics (RMSE, MAE) are reasonable values
