from character import Character
from charactertype import CharacterType
from card import Card
from cardsuit import Cardsuit
from cardtype import Cardtype, Cardtypes
import random
from datastructures.bag import Bag

clubs = []
hearts = []
spades = []
diamonds = []
multideck = Bag()
"""creating all possible cards in a 52-card deck"""
for i in Cardtypes:
    card = Card(Cardtype=i, value= None, suit= Cardsuit.CLUBS)
    clubs.append(card)
for i in Cardtypes:
    card = Card(Cardtype=i, value= None, suit= Cardsuit.HEARTS)
    hearts.append(card)
for i in Cardtypes:
    card = Card(Cardtype=i, value= None, suit= Cardsuit.SPADES)
    spades.append(card)
for i in Cardtypes:
    card = Card(Cardtype=i, value= None, suit= Cardsuit.DIAMONDS)
    diamonds.append(card)