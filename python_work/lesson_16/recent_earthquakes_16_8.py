# Practice 7/4/25.
# Chapter 16 - Recent Earthquakes.
# recent_earthquakes_16_8.py
import pathlib
import json
import plotly.express as px

# Create a path to the file.
path = pathlib.Path(r'python_work\lesson_16\eq_data\eq_data_1_month_m1.geojson')
# Read the contents of the file
content = path.read_text(encoding='utf-8')
# Parse the raw text and create dict.
all_eq_data = json.loads(content)
# print(readable_content)

# Create a new path to the new file.
path = pathlib.Path(r'python_work\lesson_16\eq_data\eq_data_1_month_m1_readable.geojson')
# Convert dict back to raw json with indent of 4
readable_content = json.dumps(all_eq_data, indent=4)
# print(readable_content)
# Write the indented version to file.
path.write_text(readable_content)

# Creates dict of all earthquakes in dataset.
all_eq_dicts = all_eq_data['features']

# Extract data
lons, lats, mags, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    mags.append(eq_dict['properties']['mag'])
    eq_titles.append(eq_dict['properties']['title'])
title = all_eq_data['metadata']['title']
# print(lons[:10])
# print(lats[:10])
# print(mags[:10])
# print(eq_titles[:10])
# Create scatter plot onbject as fig.
fig = px.scatter_geo(lat=lats,
                     lon=lons,
                     size=mags,
                     title=title,
                     color=mags,
                     color_continuous_scale='inferno',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles)

fig.show()