from Drink import Drink
from datastructures.array import Array

Menu = Array(None, Drink)

HotChoco = Drink("Hot Choco", "Medium", 4.00, None)
LondonFog = Drink("London Fod", "Medium", 5.25, None)
ChaiLatte = Drink("Chai Latte", "Medium", 5.50, None)
ItalianSoda = Drink("Italian Soda", "Medium", 4.00, None)
Lemonade = Drink("Lemonade", "Medium", 4.00, None)

Menu.append(HotChoco)
Menu.append(LondonFog)
Menu.append(ChaiLatte)
Menu.append(ItalianSoda)
Menu.append(Lemonade)