import json

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, titles, lons, lats = [], [], [], []

mags = [all_eq_dict['properties']['mag'] for all_eq_dict in all_eq_dicts]
titles = [all_eq_dict['properties']['title'] for all_eq_dict in all_eq_dicts]
lons = [all_eq_dict['geometry']['coordinates'] for all_eq_dict in all_eq_dicts]
lats = [all_eq_dict['geometry']['coordinates'] for all_eq_dict in all_eq_dicts]

print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])
