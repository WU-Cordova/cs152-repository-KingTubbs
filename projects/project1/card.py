from cardtype import Cardtype
from cardsuit import Cardsuit

class Card:
    def __init__(self, Type, Value, Suit):
        self.Type = Type
        self.Value = Value
        self.Suit = Suit
    
    def __str__(self):
        return f"{self.Type.name} of {self.Suit.name}"
    
    def __repr__(self):
        return f"{self.Type.name} of {self.Suit.name}"