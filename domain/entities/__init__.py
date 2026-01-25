# Domain Entities - POPOs (Plain Old Python Objects)
# Estas son las entidades puras de negocio, sin dependencias de frameworks
from etheriavr_backend.domain.entities.user import User
from etheriavr_backend.domain.entities.artist import Artist
from etheriavr_backend.domain.entities.song import Song
from etheriavr_backend.domain.entities.practice_session import PracticeSession
from etheriavr_backend.domain.entities.user_configuration import UserConfiguration

__all__ = [
    "User",
    "Artist",
    "Song",
    "PracticeSession",
    "UserConfiguration",
]
