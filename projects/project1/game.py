from charactertype import CharacterType
from card import Card
from cardsuit import Cardsuit
from cardtype import Cardtype, Cardtypes
from cardvalues import cardvalues
import random
from multideck import multideck, make_multideck, _cards
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
        randomcard = random.choice(_cards)
        target.hand.append(randomcard)
        multideck.remove(randomcard)

    def computescore(self, target:Character):
        target.score = 0
        self.aces_present = False #Flag
        self.aces = 0 #indicates how many aces in hand
        for card in target.hand:
            if card.Type == Cardtype.ACE:
                self.aces += 1
                self.aces_present = True
            else:
                value = cardvalues[card.Type]
                target.score += value
        #accounting for the aces AFTER everything else is calculated
        target.altscore = target.score #0, 0
        if self.aces_present == True:
            for i in range(self.aces):
                self.ace_one_able = False #Flag
                self.ace_eleven_able = False #Flag
                if target.altscore + 1 <= 21:
                    #raise flag
                    self.ace_one_able = True
                if target.altscore + 11 <= 21:
                    #raise flag
                    self.ace_eleven_able = True
                if self.ace_eleven_able == True:
                    target.altscore += 11
                elif self.ace_one_able == True:
                    target.altscore += 1

    def comparescores(self):
        playerdiff = 21 - self._player.altscore
        dealerdiff = 21 - self._dealer.altscore
        print("Round has ended. Hands are revealed.")
        print(f"Player's Hand: {self._player.hand}")
        print(f"Dealer's Hand: {self._dealer.hand}")
        if playerdiff > dealerdiff:
            return f"Dealer wins! Player score: {self._player.score} | Dealer score: {self._dealer.score}"
        if playerdiff < dealerdiff:
            return f"Player wins! Player score: {self._player.score} | Dealer score: {self._dealer.score}"
        if playerdiff == dealerdiff:
            return f"Tie! Player score: {self._player.score} | Dealer score: {self._dealer.score}"

    def hit_stay_prompt(self):
        self.hit = False
        userinput = input("Would you like to hit or stay: ")
        if userinput.lower() == "hit":
            """dealt a card"""
            self.deal(self._player)
            self.hit = True   
        elif userinput.lower() == "stay":
            """nothing - next turn"""
            self.playerstay = True
        else:
            """try again please"""
            print("Could not understand. Try spelling out the whole word")
            self.hit_stay_prompt()

    def roundend(self):
        userinput = input("Would you like to play again? Yes or No: ")
        if userinput.lower() == "yes":
            player = Character(character_type = CharacterType.PLAYER, hand = [], score = 0, altscore= 0)
            dealer = Character(character_type = CharacterType.DEALER, hand = [], score = 0, altscore= 0)
            print("Welcome to Blackjack!")
            Game(player, dealer)
        elif userinput.lower() == "no":
            quit()
        else:
            print("I dont know what you mean")
            self.roundend()

    def roundstart(self):
        """randomly makes a multideck"""
        self.playerstay = False
        self.dealerstay = False
        numberofdecks = random.randrange(2,8,2)
        for i in range(numberofdecks):
            make_multideck()
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
        if self._player.altscore > self._player.score: #indicating player has ace(s)
            print(f"Player's Hand: {self._player.hand} | Score {self._player.altscore}")
        else:
            print(f"Player's Hand: {self._player.hand} | Score {self._player.score}")
        if self._dealer.altscore > self._dealer.score: #indicating dealer has 11 value ace(s)
            #print(f"DEBUGGING: Dealer's Hand: {self._dealer.hand} | Score {self._dealer.altscore}")
            if cardvalues[self._dealer.hand[0].Type] == 1:
                print(f"Dealer's Hand: [HIDDEN], {self._dealer.hand[1:]} | Score {self._dealer.altscore - cardvalues[self._dealer.hand[0].Type]- 10}?")
        else:
            #print(f"DEBUGGING: Dealer's Hand: {self._dealer.hand} | Score {self._dealer.score}")
            print(f"Dealer's Hand: [HIDDEN], {self._dealer.hand[1:]} | Score {self._dealer.score - cardvalues[self._dealer.hand[0].Type]}?")
        #player move
        while self.playerstay == False:
            self.hit_stay_prompt()
            if self.hit == True:
                self.computescore(self._player)
                if self._player.score > 21 or self._player.altscore > 21:
                    print(f"Bust! Player loses! Player's Hand: {self._player.hand} | Score {self._player.score}")
                    self.roundend()
                else:
                    if self._player.altscore > self._player.score: #indicating player has ace(s)
                        print(f"Player's Hand: {self._player.hand} | Score {self._player.altscore}")
                    else:
                        print(f"Player's Hand: {self._player.hand} | Score {self._player.score}")
        #dealer move: hits until over 17
        while self._dealer.score < 17:
            self.deal(self._dealer)
            self.computescore(self._dealer)
            if self._dealer.score > 21 or self._dealer.altscore > 21:
                print(f"Bust! Dealer loses! Dealer's Hand: {self._dealer.hand} | Score {self._dealer.score}")
                self.roundend()
            else:
                if self._dealer.altscore > self._dealer.score: #indicating dealer has 11 value ace(s)
                    print(f"Dealer's Hand: {self._dealer.hand} | Score {self._dealer.altscore}")
                    #if cardvalues[self._dealer.hand[0].Type] == 1:
                        #print(f"Dealer's Hand: [HIDDEN], {self._dealer.hand[1:]} | Score {self._dealer.altscore - cardvalues[self._dealer.hand[0].Type]- 10}?")
                print(f"Dealer's Hand: {self._dealer.hand} | Score {self._dealer.score}")
        self.dealerstay = True
        #if both stay, compare and see who wins
        print(self.comparescores())
        self.roundend()
        

