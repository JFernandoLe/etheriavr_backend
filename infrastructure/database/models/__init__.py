# Importar todas las entidades ORM para que SQLAlchemy las registre
from etheriavr_backend.infrastructure.database.models.user_entity import UserEntity
from etheriavr_backend.infrastructure.database.models.artist_entity import ArtistEntity
from etheriavr_backend.infrastructure.database.models.song_entity import SongEntity
from etheriavr_backend.infrastructure.database.models.practice_session_entity import PracticeSessionEntity
from etheriavr_backend.infrastructure.database.models.user_configuration_entity import UserConfigurationEntity

__all__ = [
    "UserEntity",
    "ArtistEntity",
    "SongEntity",
    "PracticeSessionEntity",
    "UserConfigurationEntity",
]
