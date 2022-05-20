play = True

fizz = 'james'
buzz = 'shuffley'

while play:
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{fizz}{buzz}")
        elif i % 3 == 0:
            print(f"{fizz}")
        elif i % 5 == 0:
            print(f"{buzz}")
        print(i)
    again = str(input("Do you want to run the game again, type yes or no\n"))
    if again == "no":
        play = False
        print('Thank you for running the game')
