num= int(input("Enter a number: "))
def fib(num):
    a, b = 0 ,1
    sum = 0
    while b < num:
        if b % 2 == 0:
            sum += b
            print("Even term is : ",b)
            print(sum)
        a, b = b, a+b
    return sum
print("sum of even terms is: ",fib(num))