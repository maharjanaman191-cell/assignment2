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


# Convert monthly columns into rows
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


# Convert month name → season
def season(month):
    if month in ["December", "January", "February"]:
        return "Summer"
    elif month in ["March", "April", "May"]:
        return "Autumn"
    elif month in ["June", "July", "August"]:
        return "Winter"
    else:
        return "Spring"

data_long["Season"] = data_long["Month"].apply(season)



# 1. Average temperature per season
season_avg = data_long.groupby("Season")["Temperature"].mean()

with open("average_temp.txt", "w") as f:
    for s, v in season_avg.items():
        f.write(f"{s}: {v:.2f}°C\n")


# 2. Station(s) with largest temperature range
ranges = data_long.groupby("STATION_NAME")["Temperature"].agg(lambda x: x.max() - x.min())
max_range = ranges.max()

with open("temperature_range_stations.txt", "w") as f:
    for station, value in ranges.items():
        if value == max_range:
            f.write(f"{station}: {value:.2f}°C\n")


# 3. Stability analysis
stds = data_long.groupby("STATION_NAME")["Temperature"].std()

with open("temperature_stability_stations.txt", "w") as f:
    f.write("Most Stable Station(s):\n")
    for s in stds[stds == stds.min()].index:
        f.write(f"{s}: {stds.min():.2f}°C\n")

    f.write("\nMost Variable Station(s):\n")
    for s in stds[stds == stds.max()].index:
        f.write(f"{s}: {stds.max():.2f}°C\n")
