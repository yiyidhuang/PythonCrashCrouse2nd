cities = {
    'Beijing': {
        'country': 'China',
        'population': '21.5 million',
        'fact': 'the capital of China',
    },

    'New York': {
        'country': 'USA',
        'population': '8.5 million',
        'fact': 'the largest city of United State',
    },

    'London': {
        'country': 'UK',
        'population': '8.9 million',
        'fact': 'the one of the World Financial Center',
    },
}

for city_name, city_info in cities.items():
    print('\n' + city_name + ':')
    for city_key, city_value in city_info.items():
        print('\t' + city_key + ": " + city_value)
