import json
import pandas as pd
import plotly.express as px


filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, titles, lons, lats = [], [], [], []

mags = [all_eq_dict['properties']['mag'] for all_eq_dict in all_eq_dicts]
titles = [all_eq_dict['properties']['title'] for all_eq_dict in all_eq_dicts]
lons = [all_eq_dict['geometry']['coordinates'] for all_eq_dict in all_eq_dicts]
lats = [all_eq_dict['geometry']['coordinates'] for all_eq_dict in all_eq_dicts]

data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['Longitude', 'Latitude', 'Location', 'Magnitude']
)

data.head()

fig = px.density_mapbox(data, lat='Latitude', lon='Longitude', z='Magnitude', hover_name='Location', radius=5,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="stamen-terrain")
fig.show()
