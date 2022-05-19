# https://docs.python.org/3/library/stdtypes.html#string-methods

h = 'hello world!'

double ="double quotes"
single = 'single quotes'

#print(double, single)

#print(h[3:8])

# strip
# count
# upper
# capitalize
# replace

print(h)
print(h.strip()) # removes characters from start and beginning, default if left clear is to remove whitespace
print(h.count('o')) # provides count of the string you give it
print(h.upper()) # makes the first letter uppercase
print(h.capitalize()) # capitalizes the first letter of the string
print(h.replace('o', '*')) # replaces a letter with what you give it
print(h.replace('o', 'ooo').capitalize()) # we can also combine string methods

print(h.split()) # will split a string based on what you ask. default if left blank is white space

string = 'hello. this is an example. another thing here'
print(string.split('. ')) # we can also split based on other things, here it splits based on full stop and space

string_list = string.split(". ")
print(string_list)
new_sentence = ". ".join(string_list)
print(new_sentence)

new_sentence_capitalized = ". ".join(s.capitalize() for s in string.split(". "))
print(new_sentence_capitalized)
# this code splits the string and then capitalises the first letter and then re-joins the string

# concatenation

a = 'Mr'
b = 'Blue'
c = 'Sky'

print (a + ' ' + b + ' ' + c)

d = 'Mambo'
e = 'Number'
f = 5

print(d + ' ' + e + ' ' + str(f)) # make the int '5' a str so that it can be concatenated

# f-string (formatted string)

print(f"{d} {e} {f}") # no need to change the type and also a space is just put in normally

print(f"The next song is: {d} {e} {f}")

name = "Lassie"
years = 7
height_cm = 60.2

print(f"{name} is {years} years old and {height_cm}cm tall")

