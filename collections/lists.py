shopping_list = ['bread', 'bananas', 'biscuits', 'oat milk']

print(shopping_list)

print(shopping_list[::-1])  # prints the list in reverse order

shopping_list[0] = 'sugar'  # changes the first item of the list

print(shopping_list)

shopping_list.append('cereal')  # adds to the end of the list
print(shopping_list)

shopping_list.remove("bananas")  # removes the first instance of the given thing that it finds
print(shopping_list)

print(shopping_list.pop())  # takes a given thing (default last item) prints it and then removes it from the list
print(shopping_list)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)

print(nested_list[1])  # gives the second list

print(nested_list[1][0])  # gives the first value of the second list

