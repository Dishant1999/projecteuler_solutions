def func(n):
    i = n
    ans = 0
    while i >= 1:
        j = n
        while j >= 1:
            k = i * j
            if palindrome(k) and ans <= k:
                ans = k
            j -= 1
        i -= 1
    return ans


def palindrome(t):
    rev = 0
    k = int(t)
    while k > 0:
        rev = rev * 10
        rev = rev + k % 10
        k = int(k / 10)
    if rev == t:
        return t
    else:
        return False


print(func(input()))
