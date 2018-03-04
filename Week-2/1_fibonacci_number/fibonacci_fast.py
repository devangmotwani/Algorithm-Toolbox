# Uses python3
def fast_fib(n):
    if n<=1:
        return n
    f_num=[]
    f_num.append(int(0))
    f_num.append(int(1))
    for i in range(2,n+1):
        temp= int(f_num[-1]+f_num[-2])
        f_num.append(int(temp))
    #for i in f_num:
    #    print (i,)
    return f_num[-1]

n = int(input())
print(str(fast_fib(n)))
