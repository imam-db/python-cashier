def add_item(items):
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
            items.append(
                {
                    "item_name": item_name,
                    "n_items": n_items,
                    "price_per_item": price_per_item,
                    "total_price": n_items * price_per_item,
                }
            )
            print(f"Item {item_name} added.")
        except ValueError:
            print("Invalid input. Item was not added.")

        # Ask if user wants to add another item
        add_another = input("Do you want to add another item? (y/n) ")
        if add_another.lower() != "y":
            break


def view_items(items):
    print("-" * 40)
    print("Item Name".ljust(20), "Quantity".ljust(10), "Price".ljust(10))
    print("-" * 40)
    for item in items:
        print(
            item["item_name"].ljust(20),
            str(item["n_items"]).ljust(10),
            str(item["total_price"]).ljust(10),
        )


def delete_item(items):
    print("Select item to delete:")
    for i, item in enumerate(items):
        print(f"{i+1}. {item['item_name']}")

    try:
        item_number = int(input("Enter item number: "))
        if item_number > len(items) or item_number < 1:
            raise ValueError
    except ValueError:
        print("Invalid selection.")
        return

    confirm = input("Are you sure you want to delete this item? (y/n) ")
    if confirm.lower() == "y":
        items.pop(item_number - 1)
        print("Item deleted.")
    else:
        print("Delete cancelled.")


def update_item(items):
    print("Select item to update:")
    for i, item in enumerate(items):
        print(f"{i+1}. {item['item_name']}")

    try:
        item_number = int(input("Enter item number: "))
        if item_number > len(items) or item_number < 1:
            raise ValueError
    except ValueError:
        print("Invalid selection.")
        return

    item = items[item_number - 1]
    print(f"Updating {item['item_name']}...")
    print("What do you want to update?")
    print("1. Item name")
    print("2. Quantity")
    print("3. Price per item")
    print("4. Cancel update")

    try:
        update_type = int(input("Enter a number: "))
        if update_type not in [1, 2, 3, 4]:
            raise ValueError
    except ValueError:
        print("Invalid selection. Update cancelled.")
        return

    if update_type == 1:
        old_name = item["item_name"]
        item_name = input("Enter new item name: ")
        if item_name == "":
            print("Item name cannot be empty. Update cancelled.")
            return
        item["item_name"] = item_name
        print(f"Item name updated from {old_name} to {item_name}.")
    elif update_type == 2:
        old_n_items = item["n_items"]
        n_items = int(input("Enter new quantity: "))
        if n_items <= 0:
            print("Quantity must be more than 0. Update cancelled.")
            return
        item["n_items"] = n_items
        print(f"Quantity updated from {old_n_items} to {n_items}.")
    elif update_type == 3:
        old_price_per_item = item["price_per_item"]
        price_per_item = int(input("Enter new price per item: "))
        if price_per_item <= 0:
            print("Price per item must be more than 0. Update cancelled.")
            return
        item["price_per_item"] = price_per_item
        print(f"Price per item updated from {old_price_per_item} to {price_per_item}.")
    else:
        return

    item["total_price"] = item["n_items"] * item["price_per_item"]


def reset_transaction(items):
    reset = input("Are you sure you want to reset the transaction? (y/n) ")
    if reset.lower() == "y":
        items.clear()
        print("Transaction reset.")
    else:
        print("Reset cancelled.")
