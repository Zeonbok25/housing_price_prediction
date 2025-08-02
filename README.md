# Spatio-Temporal Housing Price Analysis Project

This project provides a comprehensive analysis of U.S. housing prices using both traditional statistical methods and deep learning approaches. The workflow consists of two main phases: exploratory spatio-temporal analysis in R and predictive modeling using LSTM neural networks in Python.

## Project Workflow

The analysis examines housing price patterns across different U.S. states over time, incorporating both spatial and temporal dimensions to understand market dynamics and predict future price trends.

### Phase 1: Statistical Analysis in R
- Exploratory data analysis and visualization
- Spatial autocorrelation analysis (Moran's I, LISA)
- Time series forecasting (ARIMA/SARIMA)
- Spatio-temporal modeling (STARIMA)

### Phase 2: Deep Learning Prediction with LSTM
- LSTM neural network implementation in Python
- Multi-state housing price prediction
- Performance evaluation and forecasting
- Future price trend analysis

## Getting Started

### For R Analysis
Please refer to **[testing-guide-R.md](testing-guide-R.md)** for:
- Software requirements and package installation
- Data setup instructions
- Step-by-step analysis execution
- Troubleshooting tips

### For LSTM Modeling
Please refer to **[lstm-guide-python.md](lstm-guide-python.md)** for:
- Python environment setup
- LSTM model implementation
- Running instructions and expected outputs
- Results interpretation

## Data Requirements

- Main dataset: `price_coords_16y.csv` (16 years of U.S. housing price data)
- Auxiliary data: U.S. state shapefiles for spatial visualization

## Project Structure

```
project/
├── data/
│   ├── price_coords_16y.csv
│   └── tl_2023_us_state/
├── testing-guide-R.md          # Detailed R analysis guide
├── lstm-guide-python.md        # Detailed LSTM modeling guide
└── README.md                   # This file
```

Follow the guides in sequence: start with R analysis for data exploration and statistical modeling, then proceed to LSTM modeling for deep learning-based predictions.