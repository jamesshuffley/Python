data_eng_37 = {
    'course_name': 'Data Engineering 37',
    'client': 'Home Office',
    'trainer': {
        'name': 'David',
        'energy_levels': 'low'
    }
}

print(data_eng_37, type(data_eng_37))

print(data_eng_37['client'])  # Dictionary name [key]


data_eng_37["trainer"]['name'] = 'David Harvey'
data_eng_37['trainees'] = ['James', 'Darnell', 'Emma', 'Munir']

print(data_eng_37)

print(data_eng_37['trainer']['energy_levels'])


