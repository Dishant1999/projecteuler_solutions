def fib(l, arr =[0,1]):
    j = 0
    i = 0
    Sum=0
    while j<l:
        # calculate fibonacci numbers with in place swapping
        j = arr[i] + arr[i + 1]
        arr[i]=arr[i+1]
        arr[i+1]=j
        #check for even numbers
        if arr[i]%2 == 0:
            Sum+=arr[i]
    return Sum
    
print(fib(40000000))
