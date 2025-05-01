from Drink import Drink
from OrderItem import OrderItem

class CustomerOrder:
    def __init__(self, name = str, order = OrderItem):
        self.name = name
        self.order = order