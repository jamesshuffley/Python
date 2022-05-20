# age = 13
# has_ticket = True

# if age >= 15 and has_ticket:
#    print('You can watch this film')
# else:
#    print('You can\'t watch this film, you need to be at least 15 and have a ticket')

film_rating = '15'

if film_rating.upper() == 'U':
    print('Titles rated bbfc-uc have been classified suitable for all.')
elif film_rating == 'PG':
    print('General viewing, but some scenes may be unsuitable for young children.')
elif film_rating == '12' or film_rating.upper() == '12A':
    print('No-one younger than 12 may rent or buy a \'12\' rated video or DVD. Responsibility for allowing under-12s '
          'to view lies with the accompanying or supervising adult.')
elif film_rating == '15':
    print('Titles rated bbfc-15 are suitable only for 15 years and over. No-one younger than 15 may see a \'15\' film '
          'in a cinema. No-one younger than 15 may rent or buy a \'15\' rated video or DVD.')
elif film_rating == '18':
    print(
        'Titles rated bbfc-18 are suitable only for adults. No-one younger than 18 may see an \'18\' film in a '
        'cinema. No-one younger than 18 may rent or buy an \'18\' rated video.')
else:
    print('This is not a rating, please enter U, 12, 12A, 15 or 18')
