from game import Game
from character import Character
from charactertype import CharacterType

#create characters
derec = Character(name = "Derec", character_type = CharacterType.WARRIOR, health = 100, attack_power = 5)
kole = Character(name = "Kole", character_type= CharacterType.ROGUE, health = 50, attack_power = 10)

#start game
game = Game(derec, kole)
game.start_battle()