num = int(input("Enter a number: "))
def sumprime(num):
    sum =0
    for i  in range(2, num+1):
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            print("Term is: ",i)
            sum += i
    return sum
print("Sum of prime numbers is: ",sumprime(num))