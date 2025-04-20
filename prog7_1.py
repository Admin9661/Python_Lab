def charcount(fname):
    count = {}
    with open(fname,"r") as file:
        for char in file.read():
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    return count

def typecheck(freq):
    text = ''.join(freq.keys())
    if "def" in text:
        print("A python file")
    elif "#include" in text:
        print("A C file")
    else:
        print("Any text file")

freq = charcount("test_file.txt")
typecheck(freq)
