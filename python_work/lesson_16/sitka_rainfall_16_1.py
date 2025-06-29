# Practice 6/26/25.
# Chapter 16 - Sitka Rainfall.
# sitka_rainfall_16_1.py

from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('python_work\lesson_16\weather_data\sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

def get_indices():
    for index, column_header in enumerate(header_row):
        print(index, column_header)

# get_indices()

# Extract daily rainfall amounts.
dates, rainfall = [], []
for row in reader:
    the_date =  datetime.strptime(row[2], '%Y-%m-%d')
    try:
        percipitation = float(row[5])
    except ValueError:
        print(f'Missing data for {the_date}')
    else:
        dates.append(the_date)
        rainfall.append(percipitation)

# Plot the amount of rainfall.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, color='blue')

# Format plot.
ax.set_title('Daily Rainfall, 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Rainfall', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()