class Song:
    """Class to represent a song

    Attributes:
        title (str): The tittle of the song
        artist (Artist): an artist object
        duration (int): the duration of the song in seconds
    """

    def __init__(self, title, artist, duration=0):
        """Song init method

        Args:
            title (str): Initialises the title attribute
            artist (Artist): an Artist object representing the songs creator
            duration (Optional[int]): initial value dor the duration attribute
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Artist:
    """Basic class to store artist details

    Attributes:
        name (str): the name of the artist
        albums (List[Album]): a list of the albums by the artist

    Methods:
        add_album: use to add a new album to artists albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list

        Args:
            album (Album): album object to add to the list
            if album is already present, it will not be added again
        """
        self.albums.append(album)


class Album:
    """" Class to represent an Album, using its tracklist

    Attributes:
        name (str): the name of the album
        year (int): release year
        artist (Artist): artist name
            If not specified, the artist will default to an "Various Artists".
        tracks (List[Song]): a list of the songs on the album

    Methods:
        add_song: used to add a new song to the album's track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song): a song to add
            position (Optional[int]): if specified, the song will be added to that position
                otherwise will be added to the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)


if __name__ == '__main__':
    load_data()
