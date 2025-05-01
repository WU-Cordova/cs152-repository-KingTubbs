1. Data structure choices for each component (Menu, Customer Order, Order Confirmation, Open Orders Queue, Completed Orders), and justifications for your choices. Your justifications should include complexity analysis and trade-offs.

Menu	            A fixed list of 5 Bistro drinks
- Array as the list will be fixed and an array is an easy way to store it
- Bag if not fixed (ie, changed every day or depending on availability)

Customer Order	    Contains customer name and list of ordered drinks
- Linked list for easy insertion to handle the dynamic nature of conversation

Order Confirmation	Allows repeating the order back to the customer
- ListStack as last-in, first-out allows for customer to easily recall their orders (they need to backtrack less)

Open Orders Queue   Queue of submitted orders waiting to be marked complete
- CircularQueue as the first-in, first-out system will be efficient for handling complete orders

Completed Orders	Records all completed orders for end-of-day report
- Deque as it allows for efficient addition at the front via append, and removal at the end via pop

2. Instructions to run the program.


3. Sample run(s) as screenshot(s) or pasted output.

4. Any known bugs or limitations.

5. What you’d add next if you had more time.