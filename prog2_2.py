import sys

arg = sys.argv[1:]
if len(arg) != 2:
    raise TypeError("Two arguments compulsory!!!!!")

val = [int(x) for x in arg]
print("Sum of Passed arguments :", val[0] + val[1])