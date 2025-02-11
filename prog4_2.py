# Define the sequences
my_list = [1, 2, 3, 4, 5]
my_tuple = (10, 20, 30, 40, 50)
my_string = "Hello"

# Using while loop
print("Iterating over the list:")
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

print("\nIterating over the tuple:")
i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1

print("\nIterating over the string:")
i = 0
while i < len(my_string):
    print(my_string[i])
    i += 1

# Using for loop
print("Iterating over the list:")
for item in my_list:
    print(item)

print("\nIterating over the tuple:")
for item in my_tuple:
    print(item)

print("\nIterating over the string:")
for char in my_string:
    print(char)
