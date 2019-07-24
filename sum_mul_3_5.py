def func_three(y):
    if y==0:
        # print y
        return y
    else:
        if y%3==0:
            print "if"
            print y
	    return y+func_three(y-1)
        else:
            print "else"
	    print y
            return func_three(y-1)

result=func_three(1000)
print result
