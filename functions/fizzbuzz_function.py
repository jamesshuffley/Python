# FizzBuzz game using functions to package it up

def fizzbuzz_line(num: int):
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    return str(num)


def fizzbuzz_game():
    for i in range(int(user_range) + 1):
        print(fizzbuzz_line(i))


play = True

while play:
    user_range = input("What number would you like the game to go up to?\n")

    print(fizzbuzz_game())

    answer = None
    while answer not in ("yes", "no"):
        answer = input("Do you want to run the game again, type yes or no\n")
        if answer.lower() in ("yes", "y"):
            break
        elif answer.lower() in ("no", "n"):
            print('Thank you for running the game')
            play = False
        else:
            print("Sorry that is not a valid response, please type yes or no\n")
