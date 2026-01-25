class Song:
    def __init__(
        self,
        song_id: int = None,
        artist_id: int = None,
        title: str = None,
        musical_genre: str = None,
        musical_key: str = None,
        original_tempo: int = None,
        duration: int = None,
        file_path: str = None,
    ):
        self.song_id = song_id
        self.artist_id = artist_id
        self.title = title
        self.musical_genre = musical_genre
        self.musical_key = musical_key
        self.original_tempo = original_tempo
        self.duration = duration
        self.file_path = file_path

        # Relaciones lógicas (no ORM)
        self.artist = None
        self.practice_sessions = []
