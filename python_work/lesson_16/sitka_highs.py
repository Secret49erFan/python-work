from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

def _get_indices():
    for index, column_header in enumerate(header_row):
        print(index, column_header)

def _header_check(header_row, header):
    try:
        return header_row.index(header)
    except ValueError:
        print(f'{header} not in list!')

path = Path('python_work/lesson_16/weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Move the reader to the first row of data.
title_row = next(reader)

indices = {column: index for index, column in enumerate(header_row)}
tmax_index = indices.get('TMAX')
tmin_index = indices.get('TMIN')
name_index = indices.get('NAME')
date_index = indices.get('DATE')

# Extract dates and high temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    high = int(row[tmax_index])
    low = int(row[tmin_index])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
station_name = title_row[name_index]
ax.set_title(f'{station_name}\nDaily High and Low Temperatures, 2021', fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature(F)', fontsize=16)
ax.set_ylim(0, 135)
ax.tick_params(labelsize=16)

plt.show()