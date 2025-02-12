from charactertype import CharacterType
from card import Card
from cardsuit import Cardsuit
from cardtype import Cardtype, Cardtypes
from cardvalues import cardvalues
import random
from multideck import multideck, clubs, spades, hearts, diamonds
from character import Character 

class Game:
    """manages blackjack logic"""
    def __init__(self, player:Character, dealer:Character):
        """initiate the game with two characters and the multideck"""
        self._player = player
        self._dealer = dealer
        self.dealerstay = False
        self.playerstay = False
        self.roundstart()
        
    def deal(self, target:Character):
        randomcard = random.choice(multideck)
        target.hand.append(randomcard)
        multideck.remove(randomcard)

    def computescore(self, target:Character):
        if target.character_type == CharacterType.PLAYER:
            self.aces_present = False
            self.aces = 0
            for card in target.hand:
                if card.Type == Cardtype.ACE:
                    self.aces += 1
                    self.aces_present = True
                else:
                    value = cardvalues[card]
                    target.score += value
            #accounting for the aces
            if self.aces_present == True:
                target.altscore = target.score
                for i in range(self.aces):
                    target.score += 1
                    target.altscore += 11
    
    def comparescores(self):
        playerdiff = 21 - self._player.score
        dealerdiff = 21 - self._dealer.score
        if playerdiff > dealerdiff:
            return f"Dealer wins! Player score: {self._player.score} | Dealer score: {self._dealer.score}"
        if playerdiff < dealerdiff:
            return f"Player wins! Player score: {self._player.score} | Dealer score: {self._dealer.score}"
        if playerdiff == dealerdiff:
            return f"Tie! Player score: {self._player.score} | Dealer score: {self._dealer.score}"

    def hit_stay_prompt(self):
        self.hit = False
        userinput = input("Would you like to hit or stay? (please type hit or stay)")
        if userinput.lower == "hit":
            """dealt a card"""
            self.deal(self._player)
            self.hit = True   
        elif userinput.lower == "stay":
            """nothing - next turn"""
            self.playerstay = True
        else:
            """try again please"""
            print("Could not understand. Try spelling out the whole word")
            self.hit_stay_prompt()

    def roundstart(self):
        """randomly makes a multideck"""
        self.end = False
        self.playerstay = False
        self.dealerstay = False
        numberofdecks = random.randrange(2,8,2)
        for i in range(numberofdecks):
            for card in clubs:
                multideck.add(card)
            for card in hearts:
                multideck.add(card)
            for card in spades:
                multideck.add(card)
            for card in diamonds:
                multideck.add(card)
        """two cards dealt to both player and dealer"""
        for i in range(2):
            self.deal(self._player)
        for i in range(2):
            self.deal(self._dealer)
        #compute scores of each characters' hands
        self.computescore(self._player)
        self.computescore(self._dealer)
        #display information, hiding dealer's first card
        print("Initial Deal:")
        print(f"Player's Hand: {self._player.hand} | Score {self._player.score}")
        print(f"Dealer's Hand: [HIDDEN] {self._dealer.hand[1:]} | Score {self._dealer.score - cardvalues[self._dealer.hand[0]]}")
        #player move
        while self.playerstay == False:
            self.hit_stay_prompt()
            if self.hit == True:
                self.computescore(self._player)
                print(f"Player's Hand: {self._player.hand} | Score {self._player.score}")
        #dealer move: hits until over 17
        while self._dealer.score < 17:
            self.deal(self._dealer)
            self.computescore(self._dealer)    
            print(f"Dealer's Hand: [HIDDEN] {self._dealer.hand[1:]} | Score {self._dealer.score - cardvalues[self._dealer.hand[0]]}")
        self.dealerstay = True
        #if both stay, compare and see who wins
        print(self.comparescores())
        userinput = input("Would you like to play again? Yes or No")
        if userinput.lower == "yes":
            Game()
        elif userinput.lower == "no":
            print("THEN LEAVE!!!")
        else:
            print("I dont know what you mean")

