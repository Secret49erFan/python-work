# PRACTICE 1/22/25 #
# CHAPTER 8 - ALBUM #

def make_album(album_songs = None):
    ''' RECORD AN ALBUM IN DICTIONARY FORMAT '''
    active = True
    album_dict = {} # INITIALIZE THE DICTIONARY #
    
    while active:
        artist_name = input('Please enter an artist name. Enter "q" to quit. ') # PROMPT FOR NAME #
        if artist_name == 'q':
            active = False
            continue
        album_title = input('Please enter an album name. Enter "q" to quit. ') # PROMPT FOR TITLE #   
        if album_title == 'q':
            active = False
            continue
        while True: # LOOPS THRU ALBUM_SONG_INPUT PROMPT UNTIL A VALID NUMBER IS PROVIDED #
            album_songs_input = input('Please enter an amount of songs. Leave blank for no songs or enter "q" to quit. ') # PROMPT FOR SONGS #
            if album_songs_input == 'q': # QUITS PROGRAM IF USER ENTERS 'Q' #
                active = False # SET FLAG TO FALSE AND END PROGRAM #
                break # EXIT THE LOOP #
            if album_songs_input == '': # SET ALBUM_SONGS TO NONE IF LEFT BLANK #
                album_songs = None # SET TO DEFAULT #
                break # EXIT THE LOOP #
            try:
                album_songs = int(album_songs_input) # CHECKS TO SEE IF ALBUM_SONG_INPUT IS CONVERTABLE TO INT #
                break # EXIT THE LOOP #
            except ValueError:
                print ('Please enter a valid number for the amount of songs.') # PROMPT USER TO RE ENTER A VALID NUMBER #

        if not active:
            break

        album_dict['name'] = artist_name
        album_dict['title'] = album_title
        album_dict['songs'] = album_songs
        
        print(album_dict)

    return album_dict

make_album()