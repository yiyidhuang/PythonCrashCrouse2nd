favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# 1
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}")

# 2
# for name, language in favorite_languages.items():
#    print(f"{name.title()}'s favorite language is {language.title()}.")

# for name in favorite_languages.keys():
#    print(name.title())

# 3
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# 4
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# 5
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# 6
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# 7
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
