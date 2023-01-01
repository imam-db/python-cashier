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
        total_price = sum([item["total_price"] for item in self.items])
        if total_price > 500000:
            discount = total_price * 0.1
        elif total_price > 300000:
            discount = total_price * 0.08
        elif total_price > 200000:
            discount = total_price * 0.05
        else:
            discount = 0
        final_price = total_price - discount
        
        print("-"*40)
        print("Item Name".ljust(20), "Quantity".ljust(10), "Price".ljust(10))
        print("-"*40)
        for item in self.items:
            print(item["item_name"].ljust(20), str(item["n_items"]).ljust(10), str(item["total_price"]).ljust(10))
        print("-"*40)
        print(f"Total price before discount: {total_price}")
        print(f"Discount: {discount}")
        print(f"Final price: {final_price}")

    """
    The add_item method allows the user to add an item to the list by prompting for the item name, quantity, and price per item. 
    If the input is invalid, the item is not added. 
    The user can choose to add multiple items.
    """
    def add_item(self):
        while True:
            try:
                item_name = input("Enter item name: ")
                if item_name == "":
                    raise ValueError
                n_items = int(input("Enter quantity: "))
                if n_items <= 0:
                    raise ValueError
                price_per_item = int(input("Enter price per item: "))
                if price_per_item <= 0:
                    raise ValueError
                self.items.append({
                    "item_name": item_name,
                    "n_items": n_items,
                    "price_per_item": price_per_item,
                    "total_price": n_items * price_per_item
                })
                print(f"Item {item_name} added.")
            except ValueError:
                print("Invalid input. Item was not added.")
            
            # Ask if user wants to add another item
            add_another = input("Do you want to add another item? (y/n) ")
            if add_another.lower() != "y":
                break

    """
    The view_items method prints a summary of all items in the list, including the item name, quantity, and price.
    """
    def view_items(self):
        print("-"*40)
        print("Item Name".ljust(20), "Quantity".ljust(10), "Price".ljust(10))
        print("-"*40)
        for item in self.items:
            print(item["item_name"].ljust(20), str(item["n_items"]).ljust(10), str(item["total_price"]).ljust(10))
    
    """
    The delete_item method allows the user to select an item from the list to delete by its number. 
    If the selection is invalid, the delete operation is cancelled.
    """
    def delete_item(self):
        print("Select item to delete:")
        for i, item in enumerate(self.items):
            print(f"{i+1}. {item['item_name']}")
            
        try:
            item_number = int(input("Enter item number: "))
            if item_number > len(self.items) or item_number < 1:
                raise ValueError
        except ValueError:
            print("Invalid selection.")
            return
        
        self.items.pop(item_number-1)
    
    """
    The update_item method allows the user to select an item from the list to update by its number. 
    If the selection is invalid, the update operation is cancelled. 
    The user is then prompted to enter new values for the item name, quantity, and price per item. 
    If any of the inputs are invalid, the update is cancelled.
    """
    def update_item(self):
        print("Select item to update:")
        for i, item in enumerate(self.items):
            print(f"{i+1}. {item['item_name']}")
        
        try:
            item_number = int(input("Enter item number: "))
            if item_number > len(self.items) or item_number < 1:
                raise ValueError
        except ValueError:
            print("Invalid selection.")
            return
        
        item = self.items[item_number-1]
        print(f"Updating {item['item_name']}...")
        item_name = input("Enter new item name: ")
        if item_name == "":
            print("Item name cannot be empty. Update cancelled.")
            return
        n_items = int(input("Enter new quantity: "))
        if n_items <= 0:
            print("Quantity must be more than 0. Update cancelled.")
            return
        price_per_item = int(input("Enter new price per item: "))
        if price_per_item <= 0:
            print("Price per item must be more than 0. Update cancelled.")
            return
        
        item.update({
            "item_name": item_name,
            "n_items": n_items,
            "price_per_item": price_per_item,
            "total_price": n_items * price_per_item
        })
    
    """
    The reset_transaction method clears the list of items in the current transaction, effectively starting a new transaction.
    """
    def reset_transaction(self):
        reset = input("Are you sure you want to reset the transaction? (y/n) ")
        if reset.lower() == "y":
            self.items = []
            print("Transaction reset.")
        else:
            print("Reset cancelled.")

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