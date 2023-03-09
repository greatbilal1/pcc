from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# path = Path("./weather_data/sitka_weather_2021_simple.csv")
# path = Path("./weather_data/death_valley_2021_simple.csv")
path = Path("./weather_data/sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# print(lines)

# Extract dates and high temperatures.
dates, total_rain = [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")

    try:
        print(row)
        rain = float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}.")
    else:
        dates.append(current_date)
        total_rain.append(rain)


# Plot the high and low temperatures.
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, total_rain, color="red", alpha=0.5)
# ax.plot(dates, lows, color="blue", alpha=0.5)
# ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format plot.
# ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
# title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
title = "Sitka Rainfall"
ax.set_title(title, fontsize=20)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
