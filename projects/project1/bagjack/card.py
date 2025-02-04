from dataclasses import dataclass
from cardtype import Cardtype
from cardsuit import Cardsuit

@dataclass
class Card:
    Type: Cardtype
    Value: int
    Suit: Cardsuit