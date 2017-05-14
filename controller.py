

def parse_source(source):
    """ determines media type from command """
    commandstring = source.split()
    command = commandstring[0]

    return command


def get_media_type(command, source ):
    """ determines media type based on user input"""
    if source =='audio':
        #figure out audio interpretation
    elif source == 'txt':
        parse_source(source)



    if command == 'play':
        media_type = music
    elif command == 'show':
        media_type = movie

    return media_type










def main():






if __name__ == "__main__":
    main()
