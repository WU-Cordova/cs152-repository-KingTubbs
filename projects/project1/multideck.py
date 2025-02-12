from character import Character
from charactertype import CharacterType
from card import Card
from cardsuit import Cardsuit
from cardtype import Cardtype, Cardtypes
import random
from datastructurescopy.bag import Bag

clubs = []
hearts = []
spades = []
diamonds = []
multideck = Bag()
"""creating all possible cards in a 52-card deck"""
for i in Cardtypes:
    card = Card(i, None, Cardsuit.CLUBS)
    clubs.append(card)
for i in Cardtypes:
    card = Card(i, None, Cardsuit.HEARTS)
    hearts.append(card)
for i in Cardtypes:
    card = Card(i, None, Cardsuit.SPADES)
    spades.append(card)
for i in Cardtypes:
    card = Card(i, None, Cardsuit.DIAMONDS)
    diamonds.append(card)