1. Data structure choices for each component (Menu, Customer Order, Order Confirmation, Open Orders Queue, Completed Orders), and justifications for your choices. Your justifications should include complexity analysis and trade-offs.

Menu	            A fixed list of 5 Bistro drinks
- Array as the list will be fixed and an array is an easy way to store it
- Bag if not fixed (ie, changed every day or depending on availability)

Customer Order	    Contains customer name and list of ordered drinks
- Linked list for easy insertion to handle the dynamic nature of conversation

Order Confirmation	Allows repeating the order back to the customer
- Linked list as it allows me to go through (print) each item efficienty one after another

Open Orders Queue   Queue of submitted orders waiting to be marked complete
- CircularQueue as the first-in, first-out system will be efficient for handling complete orders

Completed Orders	Records all completed orders for end-of-day report
- Deque as it allows for efficient addition at the front via append, and removal at the end via pop
- but in my program, i ended up using an array and instance varaibles as that was simplest for me to understand

2. Instructions to run the program.
When you start main on program.py, the main menu is given to you.
Input the number of the desired action.

3. Sample run(s) as screenshot(s) or pasted output.

📋Main Menu
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit
Enter your choice: 1
🍹 Bearcat Bistro Menu
1. Hot Choco - $4.0
2. London Fog - $5.25
3. Chai Latte - $5.5
4. Italian Soda - $4.0
5. Lemonade - $4.0
Enter your choice: 2
What's your name? Kole
How many drinks would you like to order? 2
Drink #1: Enter drink number (1-5): 1
Any customization for Hot Choco? None
Drink #2: Enter drink number (1-5): 2
Any customization for London Fog? Foamy
Order Summary for Kole:
- Hot Choco (Medium) - None
- London Fog (Medium) - Foamy
Confirm order? (yes/no): yes
order placed successfully
Enter your choice: 3
Open Orders:
[<CustomerOrder.CustomerOrder object at 0x00000244B56097F0>, <CustomerOrder.CustomerOrder object at 0x00000244B56099A0>]
[<CustomerOrder.CustomerOrder object at 0x00000244B56097F0>, <CustomerOrder.CustomerOrder object at 0x00000244B56099A0>]
1. Kole: ['Hot Choco (None)', 'London Fog (Foamy)']
Enter your choice: 4
[<CustomerOrder.CustomerOrder object at 0x00000244B5609340>, <CustomerOrder.CustomerOrder object at 0x00000244B5608DD0>]
[<CustomerOrder.CustomerOrder object at 0x00000244B5609340>, <CustomerOrder.CustomerOrder object at 0x00000244B5608DD0>]
Completed order for Kole
Enter your choice: 5
End of Day Report
Drink name       Qty Sold        Total Sales
Hot Choco        1             $4.0
London Fog        1             $5.25
Total Revenue:                      $9.25
Enter your choice: 6
goodbye

4. Any known bugs or limitations.
Whenever 3 or 4 is done, I end up with weird "[<CustomerOrder.CustomerOrder object at 0x00000244B56097F0>, <CustomerOrder.CustomerOrder object at 0x00000244B56099A0>]" being outputted alongside the desired output. The program works fine, but I never found a way to get rid of this weird printed statement.

Also, the end of day report is a little asymmetrical as I wasn't able to figure out how to make it symmetrical, but it still is functional.

5. What you’d add next if you had more time.
- A more visually-appealing interface for the operator / customer
- More usage of datastructures I wasn't able to implement due to lack of knowledge on how to apply them (program still works but I could've used more applications of other datastructures)
- Maybe an option to edit or remove current orders entirely, in case customers request it