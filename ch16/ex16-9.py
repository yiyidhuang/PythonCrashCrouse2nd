import plotly.graph_objects as go
import pandas as pd

data = pd.read_csv('data/world_fires_1_day.csv')
data.head()

fire_map = go.Densitymapbox(lat=data['latitude'], lon=data['longitude'], z=data['brightness'], radius=4)
fig = go.Figure(fire_map)
fig.update_layout(mapbox_style="open-street-map")
fig.show()
