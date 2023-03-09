from pathlib import Path
import csv
from datetime import datetime

import plotly.express as px

path = Path("./eq_data/world_fires_1_day.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)


# Extract and lat temperatures.
dates, lats, lons = [], [], []
for row in reader:
    current_date = datetime.strptime(row[5], "%Y-%m-%d")
    try:
        lat = float(row[0])
        lon = float(row[1])
    except ValueError:
        print(f"Missing data for {current_date}.")
    else:
        dates.append(current_date)
        lats.append(lat)
        lons.append(lon)

title = "World Fires"
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    title=title,
)
fig.show()
