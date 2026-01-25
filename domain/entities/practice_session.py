class PracticeSession:
    def __init__(
        self,
        session_id: int = None,
        user_id: int = None,
        song_id: int = None,
        practice_datetime: str = None,
        practice_mode: str = None,  # "piano" o "canto"
        rhythm_score: float = None,
        harmony_score: float = None,
        tuning_score: float = None,
    ):
        self.session_id = session_id
        self.user_id = user_id
        self.song_id = song_id
        self.practice_datetime = practice_datetime
        self.practice_mode = practice_mode
        self.rhythm_score = rhythm_score
        self.harmony_score = harmony_score
        self.tuning_score = tuning_score

        # Relaciones lógicas (no ORM)
        self.user = None
        self.song = None
