import eyed3


def main():
    file_name = str(input('Enter file name: ')) + '.mp3'
    answer = str(input('Enter what you want to do: '))
    audio = eyed3.load(file_name)
    if answer == 'edit':
        artist = str(input('Enter artist: '))
        album = str(input('Enter album: '))
        album_artist = str(input('Enter album artist: '))
        title = str(input('Enter title: '))
        track_num = str(input('Enter track num: '))
        add_tags(audio, new_dictionary(artist, album, album_artist, title, track_num))

    elif answer == 'check':
        print(tag_dictionary(audio))


def new_dictionary(artist, album, album_artist, title, track_num):
    tags_dict = {'artist': artist,
                 'album': album,
                 'album artist': album_artist,
                 'title': title,
                 'track num': track_num}
    return tags_dict


def tag_dictionary(audio):
    tags_dict = {'artist': audio.tag.artist,
                 'album': audio.tag.album,
                 'album artist': audio.tag.album_artist,
                 'title': audio.tag.title,
                 'track num': audio.tag.track_num}
    return tags_dict


def add_tags(audio, new_dictionary):
    try:
        audio.tag.artist = new_dictionary['artist']
        audio.tag.album = new_dictionary['album']
        audio.tag.album_artist = new_dictionary['album artist']
        audio.tag.title = new_dictionary['title']
        audio.tag.track_num = new_dictionary['track num']
        audio.tag.save()
    except KeyError:
        raise KeyError


if __name__ == '__main__':
    main()
