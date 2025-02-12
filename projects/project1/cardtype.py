from enum import Enum

class Cardtype(Enum):
    ACE = "Ace"
    TWO = "Two"
    THREE = "Three"
    FOUR = "Four"
    FIVE = "Five"
    SIX = "Six"
    SEVEN = "Seven"
    EIGHT = "Eight"
    NINE = "Nine"
    TEN = "Ten"
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King"

Cardtypes = [Cardtype.ACE,
             Cardtype.TWO,
             Cardtype.THREE,
             Cardtype.FOUR,
             Cardtype.FIVE,
             Cardtype.SIX,
             Cardtype.SEVEN,
             Cardtype.EIGHT,
             Cardtype.NINE,
             Cardtype.TEN,
             Cardtype.JACK,
             Cardtype.QUEEN,
             Cardtype.KING]
