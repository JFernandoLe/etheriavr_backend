# Domain Repositories - Interfaces (Contratos)
from etheriavr_backend.domain.repositories.IUserRepository import IUserRepository
from etheriavr_backend.domain.repositories.ISongRepository import ISongRepository
from etheriavr_backend.domain.repositories.IPracticeSessionRepository import IPracticeSessionRepository

__all__ = [
    "IUserRepository",
    "ISongRepository",
    "IPracticeSessionRepository",
]
