import eyed3


def input_mp3_file_name(mp3_file_name):
    file_split = str(mp3_file_name).split('.')
    if len(file_split) == 1 or file_split[len(file_split)-1] != 'mp3':
        raise TypeError('Invalid file type')
    else:
        try:
            audiofile = eyed3.load(mp3_file_name)
            return audiofile
        except OSError:
            raise OSError('file not found')


def get_tag(audiofile):
    tags_dict = {'artist': audiofile.tag.artist,
                 'album': audiofile.tag.album,
                 'album artist': audiofile.tag.album_artist,
                 'title': audiofile.tag.title,
                 'track num': audiofile.tag.track_num}
    return tags_dict


def set_tag(audiofile, tags_dict):
    try:
        audiofile.tag.artist = tags_dict['artist']
        audiofile.tag.album = tags_dict['album']
        audiofile.tag.album_artist = tags_dict['album artist']
        audiofile.tag.title = tags_dict['title']
        audiofile.tag.track_num = tags_dict['track num']
        audiofile.tag.save()
    except KeyError:
        raise KeyError('Key error')


def main():
    mp3_file_name = str(input('Enter path or mp3-file name: '))
    audiofile = input_mp3_file_name(mp3_file_name)
    audiofile_tags = get_tag(audiofile)



if __name__=="__main__":
    main()