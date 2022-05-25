class Category:
    def __init__(self, category):
        self.record = []
        self.__balance = 0
        self.category = category

    def check_funds(self, amount):
        """checks to see if the inputted amount is greater than the balance of the category
        if it is, it false if not true, this can be used standalone but is also used later in the
        withdrawal and transfer defs to check if the required action can take place (to prevent a minus balance)"""
        if self.__balance < amount:
            return False
        else:
            return True

    def deposit(self, amount, description=""):
        """firstly adds the amount to the category balance and then adds the amount and description
        of the deposit (if inputted) to the record list which is used later in the __str__ formatting.
        The default for the description is nothing meaning if nothing is inputted the description
        will be blank"""
        self.__balance += amount
        self.record.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """firstly uses the check_funds def to ensure the withdrawal doesn't go into the minus. if true,
        the amount is taken away from the balance and then the record is again updated with the amount
        and description of the withdrawal (if inputted) to the record list which is used later
        in the __str__ formatting"""
        if self.check_funds(amount):
            self.__balance -= amount
            self.record.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        """the getter for the balance, formatted for easier reading"""
        return f"{self.category} balance is £{self.__balance}"

    def transfer(self, amount, category):
        """checks to see if the transfer amount is greater than funds. if not, the amount it subtracted
         and then added to the requested category, and this is added to the record list"""
        if self.check_funds(amount):
            self.__balance -= amount
            self.record.append({"amount": -amount, "description": "TRANSFER TO " + category.category})
            category.__balance += amount
            category.record.append({"amount": amount, "description": "TRANSFER FROM " + self.category})
            return True
        else:
            return False

    def __str__(self):
        """creates the formatted string for print(category_name). takes an empty result, gives it a heading
        then for category it runs through the record, displaying each description and amount in a format"""
        result = ""
        result += f"--------- {self.category} ---------\n"
        for i in self.record:
            amount = 0
            description = ""
            for k, v in i.items():
                if k == "amount":
                    amount = v
                elif k == "description":
                    description = v
            if len(description) > 25:
                description = description[:25]
            amount = f"£{format(float(amount), '.2f')}"
            if len(amount) > 8:
                amount = amount[:8]
            result += description + str(amount).rjust(35 - len(description)) + "\n"
        result += f"Total: £{format(float(self.__balance), '.2f')} \n"
        return result


if __name__ == "__main__":
    food = Category("Food")
    food.deposit(100, "deposit")
    food.withdraw(4.14, "bread, milk")
    food.withdraw(30.50, "meal with friend")
    food.deposit(15.25, 'split meal with friend')

    clothing = Category("Clothing")
    food.transfer(40, clothing)
    clothing.withdraw(25.55, "t-shirt and jeans")

    entertainment = Category("Entertainment")
    entertainment.deposit(150, "deposit")
    entertainment.withdraw(30, "bowling with friends")
    entertainment.deposit(50, "money from birthday")

    print(food)
    print(clothing)
    print(entertainment)

    print(food.get_balance())
    print(clothing.get_balance())
    print(food.check_funds(200))
