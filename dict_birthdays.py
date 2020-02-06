birthdays = {
    'Luke Skywalker': '5/24/19',
    'Obi-Wan Kenobi': '3/11/57',
    'Darth Vader': '4/1/41'
}

if 'Yoda' not in birthdays:
    birthdays['Yoda'] = 'Unknown'
if ['Darth Vader'] != birthdays:
    birthdays['Yoda'] = 'Unknown'

for details in birthdays:
    print(details, birthdays[details])
