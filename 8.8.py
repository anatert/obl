def make_album(artist, name_album, count_track=''):
    albums = {'artist': artist.title(), 'track': name_album.title()}
    if count_track:
        albums['count_track'] = count_track
    return albums

while True:
    print("if you want to close the program print(q)")
    artist = input("artist:")
    if artist == 'q':
        break
    name_album = input("name_album:")
    if name_album == 'q':
        break
    album = make_album(artist, name_album)
    print(album)
