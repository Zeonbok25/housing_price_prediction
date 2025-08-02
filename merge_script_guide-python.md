
#  How to Test the Coordinate–Price Merge Script

This script merges U.S. **state-level housing price data** with corresponding **geographic coordinate data** to generate a unified dataset for spatio-temporal analysis.

---

##  Input Requirements

Place the following two files inside the `./data/` directory:

### 1. `State_zhvi_bdrmcnt_2_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv`

- **Description**: Contains monthly housing prices for each U.S. state.
- **Key Column**: `NAME` (State name), which will be used for joining.
- **Other Columns**: Time series of housing prices, typically starting from the 21st column onward (e.g., `"2000-01"` to `"2024-12"`).

### 2. `tl_2023_us_state.csv`

- **Description**: Geographic information for U.S. states, typically downloaded from [data.gov](https://www.data.gov/).
- **Key Column**: `NAME` (State name), must match with the price data.
- **Other Columns**: Includes `INTPTLAT` (Latitude), `INTPTLON` (Longitude), etc.

---

##  How to Run

Make sure you have **pandas** installed. Run the script:

```python
import pandas as pd

# Read housing price data
file1 = "./data/State_zhvi_bdrmcnt_2_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"
df_prices = pd.read_csv(file1)

# Read U.S. state coordinates
file2 = "./data/tl_2023_us_state.csv"
df_coords = pd.read_csv(file2)

# Merge both datasets on the 'NAME' column
df_merged = df_coords.merge(df_prices, on="NAME", how="left")

# Optionally remove rows with missing values
df_merged.dropna()

# Preview result
print(df_merged.head())

# Save merged data
df_merged.to_csv("price_coords_24y.csv", index=False)
```

---

##  Output

-  A merged CSV file will be created:  
  **`price_coords_24y.csv`**

This file includes:
- Geographic info for each state (coordinates, area, etc.)
- Monthly housing prices over 24+ years.

---

##  Notes

- Ensure both files use consistent naming in the `NAME` column (e.g., "New York" not "NY").
- The merged dataset is essential for spatial visualization and forecasting tasks (e.g., STARIMA, LSTM).
