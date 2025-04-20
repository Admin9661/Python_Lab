with open("test_file.txt","r") as file:
    text = file.readlines()
    for words in text:
        print(words[::-1])