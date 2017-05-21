import os
import gmail
from gmail import Gmail
import time
import subprocess

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
        test = song_name.rstrip()
        unread[0].read()

    else:
        #print "YOU HAVE READ EVERYTHING"
        artist = None
        test = None

    return artist, test


def check_for_media(artist,song_name):
        dirs = '/home/spadavec/Music/{}/{}.mp3'.format(artist,song_name)
        if os.path.exists(dirs):
            return True
        else:
            return False





def play_media(artist, song_name):
    """ Plays the media of the string passed to it. Supports the addition to an existing
    playlist (default), or to play now (flag --now)"""

    print 'artist {}'.format(artist)
    print 'song_name {}'.format(song_name)

    player = 'mpg321 '
    music_dir = '/home/spadavec/Music/'
    #LAGS = '-nodisp '
    cmd =  str(player + music_dir + artist + '/' + song_name + '.mp3')

    print "I'm gonna play this {}".format(cmd)
    os.system(cmd)


    print "I played that..."


def main():

    run = True

    while run:
        artist, song_name = check_email()

        if artist is not None:
            if check_for_media(artist,song_name):
                play_media(artist, song_name)
            else:
                continue

        time.sleep(10)



if __name__ == "__main__":
    main()
