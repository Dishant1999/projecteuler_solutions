def if_prime(n):
    d=3
    while d<n**0.5 + 1:
        if n%d == 0:
            return False
        d+=2
    return True


def func(a):
    ans= 2
    n=3
    k=1
    while (k<a):
        if if_prime(n):
            ans=n
            k=k+1
        n=n+2
    return ans
        
print(func(100001))
