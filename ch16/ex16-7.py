import json
import plotly.express as px
import pandas as pd


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
    data = zip(lons, lats, titles, mags), columns=['Longitude', 'Latitude', 'Location', 'Magnitude']
)

fig = px.scatter(
    data,
    x='Latitude',
    y='Longitude',
    range_x=[-200, 200],
    range_y=[-90, 90],
    title=all_eq_data['metadata']['title'],
    width=800,
    height=800,
    size='Magnitude',
    size_max=10,
    color='Magnitude',
    color_continuous_scale=px.colors.qualitative.Alphabet,
    hover_name='Location'
)

fig.write_html('global_earthquakes.html')
fig.show()

if __name__ == '__main__':
    print(mags[:5])
    print(titles[:5])
    print(lons[:5])
    print(lats[:5])
