order = True

while order:
    with open("drinks_menu") as drinks_menu:
        drinks_menu = drinks_menu.read()
        drink_order = input("What drink would you like to order? If you are finished ordering please type 'Done'\n")
        if drink_order == "Done":
            with open("drinks_order", "r") as drinks_order:
                receipt = drinks_order.read()
                print("Thank you for ordering, here is your receipt:\n")
                print(receipt)
            with open("drinks_order", "w") as file:
                file.write("")
            order = False
        elif drink_order in drinks_menu:
            with open("drinks_order", "a") as drinks_order:
                drinks_order.write(f"{drink_order}\n")
        else:
            print("Sorry this drink is not on the menu")
