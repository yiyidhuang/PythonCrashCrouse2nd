import json
import plotly.express as px
import pandas as pd

filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicts = all_eq_data['features']
mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['Longitude', 'Latitude', 'Location', 'Magnitude']
)

fig = px.scatter(
    data,
    x='Latitude',
    y='Longitude',
    # labels={'x': 'Longitude', 'y': 'Latitude'},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='Global seismic scatter map',
    size='Magnitude',
    size_max=10,
    color='Magnitude',
    hover_name='Location'
)

fig.write_html('global_earthquakes.html')
fig.show()

if __name__ == '__main__':
    print(mags[:5])
    print(titles[:5])
    print(lons[:5])
    print(lats[:5])
