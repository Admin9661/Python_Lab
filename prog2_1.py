import math as m
x1, y1 = map(int, input("Enter x1 and y1 : ").split())
x2, y2 = map(int, input("Enter x2 and y2 : ").split())

d = m.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"Distance between {x1,y1} and {x2,y2} is {d:.2f}")