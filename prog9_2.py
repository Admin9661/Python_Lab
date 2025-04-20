gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
lcm = lambda a, b: (a * b) // gcd(a, b)

print("GCD:", gcd(12,18))
print("LCM:", lcm(18,12))
