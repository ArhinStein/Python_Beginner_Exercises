def make_album(artist_name, album_title):
    artist_info = {'first': artist_name.title(),'title': album_title.title()}
    return artist_info

while True:
    print("Input details of artist to download.")
    print("(Enter 'q' to quit.)")
    
    artist_name = input("\nArtist name: ")
    album_title = input("\nTitle of album: ")
    break
print()
input_info = make_album(artist_name, album_title)
print(input_info)
print()