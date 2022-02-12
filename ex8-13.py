def build_profile(first, last, **user_info):
    """Create a dictionary including all information of the users as we know"""
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('jack', 'zack', location='princeton', field='maths')
print(user_profile)
