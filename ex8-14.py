def make_car(manufactory, type, **car_info):
    """Car informations"""
    car_info = {}
    car_info['car_manufactory'] = manufactory
    car_info['car_type'] = type
    for key, value in car_info.items():
        car_info[key] = value
    return car_info


cars = make_car('subaru', 'outback', color='blue', tow_package=True)

print(cars)
