def make_album(artist_name, album_title, album_tracks):
    artist_info = {'first': artist_name.title(),'title': album_title.title(),'tracks': album_tracks}
    return artist_info

album_info = make_album('kojo antwi', 'daddy anoma', 12)
print(album_info)