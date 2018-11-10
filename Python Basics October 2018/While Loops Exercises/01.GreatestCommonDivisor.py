def gcd(a = int(input()), b = int(input())):
    if b > a:
        return gcd(b, a)

    if a % b == 0:
        return b

    return gcd(b, a % b)
print(gcd())