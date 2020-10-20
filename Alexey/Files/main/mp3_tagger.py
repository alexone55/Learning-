import eyed3

def main():
    file_name = str(input('Enter file name: ')) + '.mp3'
    audio = eyed3.load(file_name)
    set_tag(audio, tag_dictionary(audio))



def tag_dictionary(audio):
    tags_dict = {'artist': audio.tag.artist,
                 'album': audio.tag.album,
                 'album artist': audio.tag.album_artist,
                 'title': audio.tag.title,
                 'track num': audio.tag.track_num}
    return tags_dict

def set_tag(audio, tag_dictionary):
    try:
        audio.tag.artist = tag_dictionary['artist']
        audio.tag.album = tag_dictionary['album']
        audio.tag.album_artist = tag_dictionary['album artist']
        audio.tag.title = tag_dictionary['title']
        audio.tag.track_num = tag_dictionary['track num']
        audio.tag.save()
    except KeyError:
        raise KeyError

if __name__ == '__main__':
    main()