from dataclasses import dataclass
from charactertype import CharacterType

@dataclass
class Character:
    character_type: CharacterType
    hand: list
    score: int
    altscore: int