def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


def func(a):
    a = int(a)
    ans = 1
    for i in range(1, a + 1):
        ans = lcm(i, ans)
    return ans


print(func(200))
