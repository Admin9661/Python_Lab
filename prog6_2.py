message = "welcome to the world of python programming."
words = message.split()
new_message = " ".join(words)
print(new_message)


birthdays= {
    "alice" : "10/09/2004",
    "bob" : "01/03/2004",
    "cinman" : "28/02/2004",
    "sam" : "30/11/1987"
}
name = input("Enter Name: ")

if name in birthdays.keys():
    print(f"{name}'s birthday is on {birthdays[name]}.")
else:
    print("data not found")