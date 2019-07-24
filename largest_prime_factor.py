def find(A):
    if A == 1:
        print(" 1 doesnt have any prime factors")
    i=2
    while i <=A:
        if A%i==0:
            A = A/i
            print(i)
            i=1
        i=i+1

find(5666789004566788)
