from charactertype import CharacterType
import random
from character import Character

#instantiating an Enum member
my_character_type = CharacterType.WARRIOR

#Accessing name and value
#print(my_character_type)        #output: Charactertpe.WARRIOR
#print(my_character_type.name)   # "WARRIOR"
#print(my_character_type.value)  # "Warrior"

class Game:
    """manages the dice battle game logic"""
    def __init__(self, player1: Character, player2: Character):
        """initializing the game with two players"""
        self._player1 = player1
        self._player2 = player2

    def attack(self, attacker: Character, defender: Character):
        """performs an attack where the attacker rolls a die to determine damage dealt"""
        die = random.randint(1,6)
        print(f"{attacker.name} has rolled a {die}")
        damage = die * attacker.attack_power
        defender.health -= damage
        print(f"{defender.name} has taken {damage} damage. He has {defender.health} hp remaining")
        #implement die roll (1-6) and apply scaled attack power to defender

    def start_battle(self):
        """starts a turn-based battle between two players"""
        battling = True
        while battling == True:
            self.attack(self._player1, self._player2)
            if self._player2.health <= 0:
                print(f"{self._player1.name} wins!")
                battling = False
            self.attack(self._player2, self._player1)
            if self._player1.health <= 0:
                print(f"{self._player2.name} wins!")
                battling = False
        #implement battle loop where players take turns attacking

