class Category:
    def __init__(self, category):
        self.record = []
        self.balance = 0
        self.category = category

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True

    def deposit(self, amount, description=""):
        self.record.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.balance -= amount
            self.record.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return f"£{self.balance}"

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.balance -= amount
            self.record.append({"amount": -amount, "description": "TRANSFER TO " + category.category})
            category.balance += amount
            category.record.append({"amount": amount, "description": "TRANSFER FROM " + self.category})
            return True
        else:
            return False

    def __str__(self):
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
        result += f"Total: £{format(float(self.balance), '.2f')} \n"
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
    entertainment.deposit(50, "birthday money")

    print(food)
    print(clothing)
    print(entertainment)

    print(food.get_balance())
    print(food.check_funds(200))




