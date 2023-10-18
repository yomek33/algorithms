a = int(input())
b = int(input())


def nativeGCD(a, b):
    best = 0
    for i in range(1, a+b):
        if a % i == 0 and b % i == 0:
            best = i
    return best


def euclidGCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


print(nativeGCD(a, b))
print(euclidGCD(a, b))
