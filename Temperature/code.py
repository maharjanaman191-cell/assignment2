import os
import pandas as pd

folder = "temperatures"
all_data = []

# Load all CSV files
for file in os.listdir(folder):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(folder, file))
        all_data.append(df)

data = pd.concat(all_data, ignore_index=True)

# ===============================
# Convert monthly columns into rows
# ===============================
month_columns = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

data_long = data.melt(
    id_vars=["STATION_NAME", "STN_ID", "LAT", "LON"],
    value_vars=month_columns,
    var_name="Month",
    value_name="Temperature"
)

# Remove missing values
data_long = data_long.dropna(subset=["Temperature"])

