from Drink import Drink
from datastructurescopy.array import Array

Menu = Array([], Drink)

HotChoco = Drink("Hot Choco", "Medium", 4.00, 0)
LondonFog = Drink("London Fog", "Medium", 5.25, 0)
ChaiLatte = Drink("Chai Latte", "Medium", 5.50, 0)
ItalianSoda = Drink("Italian Soda", "Medium", 4.00, 0)
Lemonade = Drink("Lemonade", "Medium", 4.00, 0)

Menu.append(HotChoco)
Menu.append(LondonFog)
Menu.append(ChaiLatte)
Menu.append(ItalianSoda)
Menu.append(Lemonade)