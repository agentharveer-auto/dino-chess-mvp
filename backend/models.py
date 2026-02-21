from dataclasses import dataclass

# Lightweight, illustrative models to demonstrate data structures for MVP.
# In a production system backed by PostgreSQL, these would be SQLAlchemy models.

@dataclass
class User:
    id: int
    username: str
    password_hash: str


@dataclass
class Game:
    id: int
    white_id: int | None
    black_id: int | None
    state_json: dict
    status: str
