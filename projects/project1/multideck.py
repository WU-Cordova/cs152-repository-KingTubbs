from character import Character
from charactertype import CharacterType
from card import Card
from cardsuit import Cardsuit
from cardtype import Cardtype, Cardtypes
from cardvalues import cardvalues
import random
from datastructurescopy.bag import Bag

#clubs = []
#hearts = []
#spades = []
#diamonds = []
multideck = Bag()
_cards = []
"""creating all possible cards in a 52-card deck"""
def make_multideck():   
    for i in Cardtypes:
        card = Card(i, cardvalues[i], Cardsuit.CLUBS)
        multideck.add(card)
        _cards.append(card)
    for i in Cardtypes:
        card = Card(i, cardvalues[i], Cardsuit.HEARTS)
        multideck.add(card)
        _cards.append(card)
    for i in Cardtypes:
        card = Card(i, cardvalues[i], Cardsuit.SPADES)
        multideck.add(card)
        _cards.append(card)
    for i in Cardtypes:
        card = Card(i, cardvalues[i], Cardsuit.DIAMONDS)
        multideck.add(card)
        _cards.append(card)
