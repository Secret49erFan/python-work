# Practice 7/4/25
# Chapter 16 - World Fires.
# world_fires_16_9.py
from pathlib import Path
import csv
import plotly.express as px
import numpy as np

def _header_check(header_row, header):
    try:
        return header_row.index(header)
    except ValueError:
        print(f'{header} not in list!')

# Create pointer to file and read line by line.
path = Path(r'python_work\lesson_16\fire_data\MODIS_C6_1_Global_7d.csv')
# lines = path.read_text(encoding='utf-8').splitlines()

# Create reader object to iterate thru lines
# reader = csv.reader(lines)
with path.open(encoding='utf-8') as f:
    reader = csv.reader(f)

    # Read first row with all headers
    header_row = next(reader)

    # Get the index and value of header_row.
    # indices = {column: index for index, column in enumerate(header_row)}
    lon_index = _header_check(header_row, 'longitude')
    lat_index = _header_check(header_row, 'latitude')
    bright_index = _header_check(header_row, 'brightness')

    # Extract longitude, latitude, and brightness.
    lons, lats, brights = [], [], []
    # Threshold filter.
    threshold = 420
    # Skip counter.
    skipped = 0
    for row in reader:
        try:
            lon = float(row[lon_index])
            lat = float(row[lat_index])
            bright = float(row[bright_index])
        except (ValueError, IndexError):
            skipped += 1
            print(f'Skipping {row}! Check data!')
            continue
        if bright > threshold:
            lons.append(lon)
            lats.append(lat)
            brights.append(bright)
    print(f'Skipped {skipped} corrupted rows.')

# Normalizes all brightness values for marker size.
sizes = np.interp(brights, (min(brights), max(brights)), (2,10))

fig = px.scatter_geo(lat=lats,
                     lon=lons,
                     size=sizes,
                     title='World Fires in the Last 30 Days.',
                     color=brights,
                     color_continuous_scale='inferno',
                     labels={'color':'Brightness'},
                     projection='natural earth',
                     hover_name=[f'Brightness: {b}' for b in brights],
                     )

fig.show()