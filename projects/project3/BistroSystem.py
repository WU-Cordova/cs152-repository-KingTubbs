from Drink import Drink
from Menu import Menu
from MainMenu import MainMenu
from OrderItem import OrderItem
from CustomerOrder import CustomerOrder
from datastructures.linkedlist import LinkedList
from datastructures.array import Array
from datastructures.arraystack import ArrayStack
from datastructures.liststack import ListStack
from datastructures.circularqueue import CircularQueue

class BistroSystem:
    def __init__(self):
        self.openorders = CircularQueue(10, LinkedList)

    def MainMenuDisplay(self):
        for line in MainMenu:
            print(line)

    def MenuDisplay(self):
        print("🍹 Bearcat Bistro Menu")
        n=1
        for drink in Menu:
            print(f"{n}. {drink.name} - ${drink.price}")
            n+=1

    def TakeOrder(self):
        nameinput = input("What's your name? ")
        orders = LinkedList(CustomerOrder)
        numberoforders = int(input("How many drinks would you like to order? "))
        for i in numberoforders:
            drinkinput = int(input(f"Drink #{1+i}: Enter drink number (1-5): "))
            while drinkinput not in [1, 2, 3, 4, 5]:
                print("invalid response, please try again")
                drinkinput = int(input(f"Drink #{1+i}: Enter drink number (1-5): "))
            customizationinput = input(f"Any customization for {Menu[drinkinput]}? ")
            ordereditem = OrderItem(Menu[drinkinput], customizationinput)
            customerorder = CustomerOrder(nameinput, ordereditem)
            orders.append(customerorder)
        #order summary
        print(f"Order Summary for{nameinput}:")
        for customerorder in orders:
            print(f"- {customerorder.order.drink.name} (Medium) - {customerorder.order.customization}")

        userinput = input(f"Confirm order? (yes/no): ")
        if userinput.upper() == "yes":
            self.openorders.append(orders)
            print("order placed successfully")
        if userinput.upper() != "yes":
            print("order has been cancelled")

    def viewopenorders(self):
        """
            Drink(name, size, price)
            OrderItem(drink, customization)
            CustomerOrder(name, order)
            orders : linkedList of customerorder
            self.openorders : circularqueue of orders    
        """
        print("Open Orders:")
        n=1
        for LinkedList in self.openorders:
            sequence = []
            for order in LinkedList:
                sequence.append(f"{order.order.drink.name} ({order.order.customization})")
            print(f"{n}. {LinkedList[0].name}: {sequence}")
            n += 1

    def markordercomplete(self):


    def MainMenuInput():
        userinput = input("Enter your choice: ")
        while userinput not in ["1", "2", "3", "4", "5", "6"]:
            print ("Invalid Response. Please choose a number between 1-6")
            userinput = input("Enter your choice: ")
        if userinput == "1":
            #Display Menu
            BistroSystem.MenuDisplay()
            BistroSystem.MainMenuInput()
        if userinput == "2":
            #Take new order
            BistroSystem.TakeOrder()
            BistroSystem.MainMenuInput()
        if userinput == "3":
            #View Open Orders
            BistroSystem.viewopenorders()
            BistroSystem.MainMenuInput()
        if userinput == "4":
            #Mark Next Order as Complete
            BistroSystem.markordercomplete()
            BistroSystem.MainMenuInput()
        if userinput == "5":
            #View End-of-Day Report
        if userinput == "6":
            #Exit


if __name__ == '__main__':
    print("Welcome to the Bistro!")
    print(" ")
    BistroSystem.MainMenuDisplay()
    BistroSystem.MainMenuInput()


