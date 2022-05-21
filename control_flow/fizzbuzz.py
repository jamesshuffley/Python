play = True

fizz = 'james'
buzz = 'shuffley'

while play:
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print(f'{fizz}{buzz}')
            continue
        elif i % 3 == 0:
            print(f'{fizz}')
            continue
        elif i % 5 == 0:
            print(f'{buzz}')
            continue
        print(i)
    answer = None
    while answer not in ("yes", "no"):
        answer = input("Do you want to run the game again, type yes or no\n")
        if answer == "yes":
            break
        elif answer == "no":
            print('Thank you for running the game')
            play = False
        else:
            print("sorry that is not a valid response, please type yes or no\n")


