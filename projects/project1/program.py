from bagjack.game import Game
from bagjack.character import Character
from bagjack.charactertype import CharacterType
from datastructures.bag import Bag

def main():
    player = Character(character_type = CharacterType.PLAYER, hand = [], score = 0)
    dealer = Character(character_type = CharacterType.DEALER, hand = [], score = 0)
    print("Welcome to Blackjack!")
    Game()

if __name__ == '__main__':
    main()
