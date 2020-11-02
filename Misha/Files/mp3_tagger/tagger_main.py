import eyed3


def input_mp3_file_name(mp3_file_name):
    file_split = str(mp3_file_name).split('.')
    if len(file_split) == 1 or file_split[len(file_split) - 1] != 'mp3':
        raise TypeError('Invalid file type')
    else:
        audiofile = eyed3.load(mp3_file_name)
        return audiofile


def get_tag(audiofile):
    tags_dict = {'artist': audiofile.tag.artist,
                 'album': audiofile.tag.album,
                 'album artist': audiofile.tag.album_artist,
                 'title': audiofile.tag.title,
                 'track num': audiofile.tag.track_num}
    return tags_dict


def set_tag(audiofile, tag_dict):
    audiofile.tag.artist = tag_dict['artist']
    audiofile.tag.album = tag_dict['album']
    audiofile.tag.album_artist = tag_dict['album artist']
    audiofile.tag.title = tag_dict['title']
    audiofile.tag.track_num = tag_dict['track num']
    audiofile.tag.save()


def main():
    mp3_file_name = str(input('Enter path or mp3-file name: '))
    audiofile = input_mp3_file_name(mp3_file_name)
    audiofile_tag = get_tag(audiofile)
    return 0


if __name__ == "__main__":
    main()
