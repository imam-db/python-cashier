from cashier_functions import check_order, add_item, view_items, delete_item, update_item, reset_transaction

class Cashier:
    """
    This is the Cashier class, which is responsible for managing a list of items and calculating the total price of an order with applicable discounts.
    The init method initializes the Cashier object with an empty list of items.
    """
    def __init__(self):
        self.items = []
    
    """
    The check_order method calculates the total price of the order by summing the total prices of all items in the order. 
    If the total price is greater than 500000, a 10% discount is applied. 
    If the total price is greater than 300000 but less than or equal to 500000, an 8% discount is applied. 
    If the total price is greater than 200000 but less than or equal to 300000, a 5% discount is applied. 
    If the total price is less than or equal to 200000, no discount is applied. 
    The final price is then calculated by subtracting the discount from the total price. 
    The check_order method also prints a summary of the order, including the item name, quantity, and price for each item, as well as the total price before and after the discount.
    """
    def check_order(self):
        check_order(self.items)

    """
    The add_item method allows the user to add an item to the list by prompting for the item name, quantity, and price per item. 
    If the input is invalid, the item is not added. 
    The user can choose to add multiple items.
    """
    def add_item(self):
        add_item(self.items)

    """
    The view_items method prints a summary of all items in the list, including the item name, quantity, and price.
    """
    def view_items(self):
        view_items(self.items)
    
    """
    The delete_item method allows the user to select an item from the list to delete by its number. 
    If the selection is invalid, the delete operation is cancelled.
    """
    def delete_item(self):
        delete_item(self.items)
    
    """
    The update_item method allows the user to select an item from the list to update by its number.
    If the selection is invalid, the update operation is cancelled.
    The user is then prompted to select which aspect of the item to update: item name, quantity, or price.
    If any of the inputs are invalid, the update is cancelled.
    """
    def update_item(self):
        update_item(self.items)
    
    """
    The reset_transaction method clears the list of items in the current transaction, effectively starting a new transaction.
    """
    def reset_transaction(self):
        reset_transaction(self.items)

    """
    The menu method displays a menu of options for the user to choose from, 
    including adding items, viewing items, deleting items, updating items, resetting the current transaction, and checking out. 
    The user can choose an option by entering its corresponding number.
    """
    def menu(self):
        
        while True:
            print("-"*40)
            print("1. Add item")
            print("2. View items")
            print("3. Delete item")
            print("4. Update item")
            print("5. Check order")
            print("6. Reset transaction")
            print("7. Quit")
            print("-"*40)
            
            try:
                selection = int(input("Enter a number: "))
            except ValueError:
                print("Invalid selection. Try again.")
                continue
            
            if selection == 1:
                cashier.add_item()
            elif selection == 2:
                cashier.view_items()
            elif selection == 3:
                cashier.delete_item()
            elif selection == 4:
                cashier.update_item()
            elif selection == 5:
                cashier.check_order()
            elif selection == 6:
                cashier.reset_transaction()
            elif selection == 7:
                break
            else:
                print("Invalid selection. Try again.")
    

cashier = Cashier()
cashier.menu()