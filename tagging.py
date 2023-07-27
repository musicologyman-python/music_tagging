import enum
from pathlib import Path
from mutagen.mp4 import MP4

class M4ATags(enum.StrEnum):

    ALBUM = "©alb"
    ALBUM_ARTIST = "aART"
    ALBUM_COVER = "covr"
    ARTIST = "©ART"
    CDDB_1 = "----:com.apple.iTunes:iTunes_CDDB_1"
    CDDB_TRACK_NUMBER = "----:com.apple.iTunes:iTunes_CDDB_TrackNumber"
    COMPILATION = "cpil"
    COMPOSER = "©wrt"
    CONDUCTOR = "----:com.apple.iTunes:CONDUCTOR"
    DATE = "©day"
    DISC_NUMBER = "disk"
    ENCODED_BY = "©too"
    ENCODING_PARAMETERS = "----:com.apple.iTunes:Encoding Params"
    GENRE = "©gen"
    ITUNES_NORMALIZATION = "----:com.apple.iTunes:iTunNORM"
    MOVEMENT = "©mvn"
    MOVEMENT_COUNT = "©mvc"
    MOVEMENT_NUMBER = "©mvi"
    PART_OF_GAPLESS_ALBUM = "pgap"
    SHOW_WORK_MOVEMENT = "shwm"
    TITLE = "©nam"
    TRACK_NUMBER = "trkn"
    WORK = "©wrk"

def get_audio_files(parent=Path.cwd()):
    return [p for p in parent.iterdir() if p.suffix == '.m4a']
    
def get_tags(audio_file):
    match audio_file:
        case MP4() as tag:
            return tag
        case Path() as p:
            return get_tags(MP4(p))
        case str() as s:
            return get_tags(MP4(s))
        case _:
            raise TypeError(f"Cannot get tags for instances of type {audio_file.__class__}.")
            
def get_tag_keys(audio_file):
    return get_tags(audio_file).keys()

def print_tags(tags):
    
    for key, value in tags:
        print(key, end=' ')
        while True:
            match input('Print value? [Y/n] ').lower().strip():
                case 'n':
                    break
                case 'y'| '':
                    print(f'    {value}')
                    break
                case _:
                    print('Invalid response')
                    continue
    
