'''def city_country(city, country):
    return f'{city.title()}, {country.title()}'

print(city_country('city', 'country'))'''

def make_album(artist, name_album, count_track=''):
    albums = {'artist': artist, 'track': name_album}
    if count_track:
        albums['count_track'] = count_track
    return albums

print(make_album('artist_1', 'name_album_1', 8))

