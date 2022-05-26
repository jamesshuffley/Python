def add_plus_one(num1, num2):
    return num1 + num2 + 1


print(add_plus_one(3, 7))

# Lambda (or anonymous) functions

addition = lambda num1, num2: num1 + num2 + 1

print(addition(5, 8))

# map

# using a for loop
savings = [234.00, 555.00, 647.25, 839.00]
bonus = []
for saving in savings:
    bonus.append(saving * 1.1)
print(bonus)


# using map
def apply_bonus(saving):
    return saving * 1.1


# w/ list
bonus_map = map(apply_bonus, savings)
print(bonus_map)

# w list
bonus_map = list(map(apply_bonus, savings))
print(bonus_map)

# lambda
bonus_lambda = list(map(lambda x: x * 1.1, savings))
print(bonus_lambda)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# use map and lambda to create a list of each number squared plus 3

square_lambda = list(map(lambda x: (x ** 2) + 3, numbers))
print(square_lambda)

jobs = ["Data Analyst", "C# Developer", "Data Engineer", "DevOps Engineer", "Data Architect"]

# produce a list of data-based roles without the word data in there
lambda_filter = filter(lambda x: "Data" in x, jobs)  # filters through and returns true if the string contains "Data
lambda_map = map(lambda x: x.replace("Data ", ""), lambda_filter)  # replaces "Data " with an empty string

print(list(lambda_map))
