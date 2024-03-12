import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth

#INTIIAL VARS TO CALL API
PLAYLIST_ID1 = 'YOUR-PLAYLIST-ID'
PLAYLIST_ID2 = 'YOUR-PLAYLIST-ID2'

scope = 'playlist-modify-public'

spotifyObject = sp.Spotify(auth_manager=SpotifyOAuth(scope=scope)) #MAKE SURE YOU MAKE THE ENVIRONMENT VARS
print('obj made')

#FIRST PLAYLIST
TRACKS = spotifyObject.playlist_items(PLAYLIST_ID1, offset=0)
print('tracks acquired')

artist_list = []
offset_var = 0

while len(TRACKS) < 100 and offset_var <= TRACKS['total']:
    try:
        print('processing playlist block:')
        TRACKS = spotifyObject.playlist_items(PLAYLIST_ID1, offset=offset_var)
        for song in TRACKS['items']:
            for artist in song['track']['artists']:
                print(artist['name'], len(artist_list))
                artist_list.append(artist['name'])
        offset_var += 132 #its just somewhat optimal without missing a song

    except:
        with open('artist_list1.txt', 'w', encoding="utf-8") as f:
            f.write(artist_list[0]+'\n'.join(artist_list))
            f.close()
          
print('first playlist analyzed')

#SECOND PLAYLIST
TRACKS2 = spotifyObject.playlist_items(PLAYLIST_ID2, offset=0)
print('tracks2 acquired')

artist_list2 = []
offset_var = 0

while len(TRACKS2) < 100 and offset_var <= TRACKS2['total']:
    try:
        print('processing playlist block:')
        TRACKS2 = spotifyObject.playlist_items(PLAYLIST_ID2, offset=offset_var)
        for song in TRACKS2['items']:
            for artist in song['track']['artists']:
                print(artist['name'], len(artist_list2))
                artist_list2.append(artist['name'])
        offset_var += 132

    except:
        with open('artist_list2.txt', 'w', encoding="utf-8") as f:
            f.write('\n'.join(artist_list2))
            f.close()
          
print('second playlist analyzed')

#MATCH
match = []

print('starting match...')
for i in artist_list:
    if i in artist_list2 and i not in match:
        match.append(i)
with open('artist_match.txt', 'w', encoding="utf-8") as f:
    f.write('\n'.join(match))
    f.close()

print('done!')
print(match)
