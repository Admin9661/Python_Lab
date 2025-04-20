with open("test_file.txt","r") as file:
    lines = file.readlines()
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)
    print("No. of lines: ",line_count)
    print("No. of words: ",word_count)
    print("No. of characters: ",char_count)