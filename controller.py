import os
import gmail
from gmail import Gmail


def check_email():
    client = Gmail()
    USERNAME = 'ifthisthenthatclone'
    PASSWORD = 'ifthisthenthat'
    client.login(USERNAME,PASSWORD)




    if client.inbox().mail(unread=True):

        unread = client.inbox().mail(unread=True)
        unread[0].fetch()
        print "The input string is {}".format(unread[0].body)
        print ""
        # FORMAT MUST BE (ARTIST, SONG NAME)

        input_string = unread[0].body
        input_split = input_string.split(',')
        artist=input_split[0].lower()
        song_name=input_split[1].lower()
        print 'artist {}'.format(artist)


        return artist,  song_name






def play_media(artist, song_name):
    """ Plays the media of the string passed to it. Supports the addition to an existing
    playlist (default), or to play now (flag --now)"""


    player = 'cvlc '
    music_dir = '~/Music/'
    cmd =  str(player + music_dir + artist + '/' + song_name + '.mp3')
    print cmd

    os.system(cmd)





def main():
    artist, song_name = check_email()
    play_media(artist, song_name)





if __name__ == "__main__":
    main()
