fav_film = {
    'film_title': 'Hot Fuzz',
    'budget_usd_mil': 12,
    'box_office_usd_mill': 80.7,
    'run_time_mins': 121,
    'release_date': '2007-02-14',
    'written_by': ['Edgar Wright', 'Simon Pegg'],
    'imbd_rating': 7.8,
    'cast': {
        'Simon Pegg': 'PC Nicholas Angel',
        'Nick Frost': 'PC Danny Butterman',
        'Jim Broadbent': 'Inspector Frank Butterman'
    }
}

# fav_film['genre'] = 'comedy'

# print(fav_film)

# print(fav_film['written_by'][1])

# print(fav_film.keys())

print(f"James's favourite film is {fav_film['film_title']} was was released on {fav_film['release_date']}. It has a "
      f"runtime of {fav_film['run_time_mins']} minutes and was written by {fav_film['written_by'][0]} and {fav_film['written_by'][1]}")

