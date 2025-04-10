from game import Game
from character import Character
from charactertype import CharacterType

def main():
    player = Character(character_type = CharacterType.PLAYER, hand = [], score = 0, altscore= 0)
    dealer = Character(character_type = CharacterType.DEALER, hand = [], score = 0, altscore= 0)
    print("Welcome to Blackjack!")
    Game(player, dealer)

if __name__ == '__main__':
    main()
