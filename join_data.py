import pandas as pd

# read house price data
file1 = "./data/State_zhvi_bdrmcnt_2_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"
df_prices = pd.read_csv(file1)

# read coords data
file2 = "./data/tl_2023_us_state.csv"
df_coords = pd.read_csv(file2)

# join two table
df_merged = df_coords.merge(df_prices, on="NAME", how="left")
df_merged.dropna()

print(df_merged.head())
df_merged.to_csv("price_coords_24y.csv", index=False)