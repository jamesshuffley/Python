# try:
#     file = open("order.txt")
# except FileNotFoundError as errmsg:
#     print("File has not been found")
#     print(errmsg)


# print(file, type(file))
#
# orders = file.readlines()
#
# print(orders)
#
# orders = list(map(lambda x: x.strip('\n'), orders))
#
# print(orders)
#
# file.close()

# with open("order.txt") as file:
#     raw_orders = file.readlines()
#     orders = list(map(lambda x: x.strip("\n"), raw_orders))
#
# print(file.closed)
#
# with open("order.txt") as file:
#     orders = file.read()
#
# print(orders)

# with open("order.txt", "w") as file:
#     file.write("This will overwrite a string of an existing file, or create a new file")
#

# with open("order.txt", "a") as file:
#     file.write("New string to write\n")

# colours = ["red", 'yellow', 'green']
#
# with open("order.txt", "a") as file:
#     file.writelines(colours)



