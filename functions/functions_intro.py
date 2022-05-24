# DRY - Don't Repeat Yourself

# Good Functions
# Name them clearly, lowercase_with_underscores (snakecase)
# Clear argument names
# Functions that don't return something return None
# Keep them small
# Use comments to explain what the function does, use
# Consider type hints


# create the function
def greeting(name='...you!'):  # this is the default, if nothing is passed in it will default to whatever is placed here
    return f'Hello, {name}!'


# call the function
result = greeting('James')
print(result)

result = greeting()
print(result)


def multiply(*nums):  # multiple arguments
    if len(nums) == 0:
        return None
    answer = 1
    for num in nums:
        answer *= num
    return answer


print(multiply(1, 1))


def kwargs_demo(**kwargs):  # Key word arguments
    print(kwargs, type(kwargs))


def total_cost(**meal_prices):
    total = 0
    for price in meal_prices.values():
        total += price
    return total


print(total_cost(
    Pizza=8.50,
    Burger=9.00,
    HotDog=9.20
))


def fizzbuzz_line(num: int):
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    return str(num)


def fizzbuzz_game():
    for i in range(1, 101):
        return fizzbuzz_line()


print(fizzbuzz_game())

