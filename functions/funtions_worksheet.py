print("\nQ1a\n")


# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1


# A1a:

def print_factors(x):
    lst = []
    for i in range(1, x + 1):
        if x % i == 0:
            lst.append(i)
    return lst


print(print_factors(12))

print("\nQ1b\n")


# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function


# A1b:

def is_factor(f, n):
    return n % f == 0 or f % n == 0


print(is_factor(12, 3))
# -------------------------------------------------------------------------------------- #


print("\nQ2a\n")


# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
# "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


# A2a:

def position(letter):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    return alphabet.index(letter)


print(position('b'))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14


# A2b:

def name_id(name):
    index = []
    for i in name:
        ind = position(i)
        index.append(str(ind))
        new_string = "".join(index)
    return new_string


print(name_id('bob'))

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)


# A2c:


# -------------------------------------------------------------------------------------- #


print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.


# A3a:

def is_prime(x):
    x = int(x)
    for i in range(2, x):
        if x % i == 0:
            return False
    return x >= 2


print(is_prime(2))


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit


# A3b:
def is_prime2(x):
    if int(x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return x >= 2
    else:
        return None


print(is_prime2(2))

# -------------------------------------------------------------------------------------- #
