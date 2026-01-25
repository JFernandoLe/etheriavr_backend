class Artist:
    def __init__(
        self,
        artist_id: int = None,
        artist_name: str = None,
    ):
        self.artist_id = artist_id
        self.artist_name = artist_name

        # Relación lógica (no ORM)
        self.songs = []
