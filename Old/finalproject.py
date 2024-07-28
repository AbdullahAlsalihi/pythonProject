

inventory = []

def add_item(name, price, quantity, category):

    x = {
        'name: ': name,
        'price:': price


    }
    inventory.append(x)
     print()

def update_item(name, price=none, quantity=none, category=none):
    for x in inventory:
        if ...:

    print()

def view_inventory():
    if not inventory:
        print('The inventory is empty')
    else:
        for x in inventory:
            .....
def remove_item(name):
    for x in inventory:
        ...........:
    print()

def search_by_category(category):
    for x ....:
        if not ...
        else:
            for loop





                def main():
                    while True:
                        print("\nInventory Management System")
                        print("1. Add Item")
                        print("2. Update Item")
                        print("3. View Inventory")
                        print("4. Remove Item")
                        print("5. Search by Category")
                        print("6. Exit")
                        choice = input("Enter your choice: ")

                        if choice == '1':
                            name = input("Enter item name: ")
                            price = float(input("Enter item price: "))
                            quantity = int(input("Enter item quantity: "))
                            category = input("Enter item category: ")
                            add_item(name, price, quantity, category)
                        elif choice == '2':
                            name = input("Enter item name to update: ")
                            price = input("Enter new price (or press enter to skip): ")
                            quantity = input("Enter new quantity (or press enter to skip): ")
                            category = input("Enter new category (or press enter to skip): ")
                            price = float(price) if price else None
                            quantity = int(quantity) if quantity else None
                            update_item(name, price, quantity, category)
                        elif choice == '3':
                            view_inventory()
                        elif choice == '4':
                            name = input("Enter item name to remove: ")
                            remove_item(name)
                        elif choice == '5':
                            category = input("Enter category to search: ")
                            search_by_category(category)
                        elif choice == '6':
                            print("Exiting the Inventory Management System.")
                            break
                        else:
                            print("Invalid choice. Please try again.")

                if __name__ == "__main__":
                    main()







































