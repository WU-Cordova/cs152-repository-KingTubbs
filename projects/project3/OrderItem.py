from Drink import Drink
class OrderItem:
    def __init__(self, drink = Drink, customization = str):
        self.drink = drink
        self.customization = customization