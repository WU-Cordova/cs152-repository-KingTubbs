from Drink import Drink
from Menu import Menu
from MainMenu import MainMenu
from OrderItem import OrderItem
from CustomerOrder import CustomerOrder
from datastructurescopy.array import Array
from datastructurescopy.arraystack import ArrayStack
from datastructurescopy.circularqueue import CircularQueue
from datastructurescopy.linkedlist import LinkedList
import copy

class BistroSystem:
    def __init__(self):
        self.openorders = CircularQueue(10, LinkedList)
        self.completed = Array([], LinkedList)
        self.completedcount = 0

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
        numberoforders = (input("How many drinks would you like to order? "))
        numberoforders = int(numberoforders)
        for i in range(numberoforders):
            drinkinput = int(input(f"Drink #{1+i}: Enter drink number (1-5): "))
            while drinkinput not in [1, 2, 3, 4, 5]:
                print("invalid response, please try again")
                drinkinput = int(input(f"Drink #{1+i}: Enter drink number (1-5): "))
            customizationinput = input(f"Any customization for {Menu[drinkinput-1].name}? ")
            ordereditem = OrderItem(Menu[drinkinput-1], customizationinput)
            customerorder = CustomerOrder(nameinput, ordereditem)
            orders.append(customerorder)
        #order summary
        print(f"Order Summary for {nameinput}:")
        for customerorder in orders:
            print(f"- {customerorder.order.drink.name} (Medium) - {customerorder.order.customization}")

        userinput = input(f"Confirm order? (yes/no): ")
        if userinput.lower() == "yes":
            self.openorders.enqueue(orders)
            print("order placed successfully")
        else:
            print("order has been cancelled")

    def viewopenorders(self):
        """
            Drink(name, size, price, qtysold)
            OrderItem(drink, customization)
            CustomerOrder(name, order)
            orders : linkedList of customerorder
            self.openorders : circularqueue of orders    
        """
        print("Open Orders:")
        n = 1
        for i in range(len(self.openorders)):
            order_list = copy.deepcopy(self.openorders).dequeue() 
            sequence = []
            for order in order_list:
                sequence.append(f"{order.order.drink.name} ({order.order.customization})")
            print(f"{n}. {order_list.front.name}: {sequence}")
            n += 1

    def markordercomplete(self):
        if self.openorders:
            self.completed.append(self.openorders.dequeue())
            print(f"Completed order for {self.completed[self.completedcount].front.name}")
            self.completedcount += 1
            for item in self.completed[self.completedcount - 1]:  # Use completedcount - 1
                item.order.drink.qtysold += 1
        else:
            print("No orders")

    def report(self):
        print("End of Day Report")
        print("Drink name       Qty Sold        Total Sales")
        total = 0
        for drink in Menu:
            if drink.qtysold > 0:
                print(f"{drink.name}        {drink.qtysold}             ${drink.qtysold * drink.price}")
                total += drink.qtysold * drink.price
        print(f"Total Revenue:                      ${total}")
    def MainMenuInput(self):
        userinput = input("Enter your choice: ")
        while userinput not in ["1", "2", "3", "4", "5", "6"]:
            print ("Invalid Response. Please choose a number between 1-6")
            userinput = input("Enter your choice: ")
        if userinput == "1":
            #Display Menu
            self.MenuDisplay()
            self.MainMenuInput()
        if userinput == "2":
            #Take new order
            self.TakeOrder()
            self.MainMenuInput()
        if userinput == "3":
            #View Open Orders
            self.viewopenorders()
            self.MainMenuInput()
        if userinput == "4":
            #Mark Next Order as Complete
            self.markordercomplete()
            self.MainMenuInput()
        if userinput == "5":
            #View End-of-Day Report
            self.report()
            self.MainMenuInput()
        if userinput == "6":
            #Exit
            print("goodbye")
            quit


if __name__ == '__main__':
    pass


