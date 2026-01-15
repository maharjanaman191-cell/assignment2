import os
import pandas as pd

# Folder where all the temperature CSV files are stored
folder = "temperatures"
# This list will hold data from every CSV file
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
        
# Apply the season function to each row
data_long["Season"] = data_long["Month"].apply(season)



# 1. Average temperature per 
# Calculate the average temperature for every season
season_avg = data_long.groupby("Season")["Temperature"].mean()

# Save the seasonal averages to a text file
with open("average_temp.txt", "w") as f:
    for s, v in season_avg.items():
        f.write(f"{s}: {v:.2f}°C\n")


# 2. Station(s) with largest temperature range
# Calculate how much temperatures vary at each station
ranges = data_long.groupby("STATION_NAME")["Temperature"].agg(lambda x: x.max() - x.min())


# Get the largest temperature range found
max_range = ranges.max()

# Write the station(s) with the largest range to a file
with open("temperature_range_stations.txt", "w") as f:
    for station, value in ranges.items():
        if value == max_range:
            f.write(f"{station}: {value:.2f}°C\n")


# 3. Stability analysis

# Showing how stable or variable temperatures are
stds = data_long.groupby("STATION_NAME")["Temperature"].std()

# Saving the most stable and most variable stations
with open("temperature_stability_stations.txt", "w") as f:
    f.write("Most Stable Station(s):\n")
    for s in stds[stds == stds.min()].index:
        f.write(f"{s}: {stds.min():.2f}°C\n")

    f.write("\nMost Variable Station(s):\n")
    for s in stds[stds == stds.max()].index:
        f.write(f"{s}: {stds.max():.2f}°C\n")
