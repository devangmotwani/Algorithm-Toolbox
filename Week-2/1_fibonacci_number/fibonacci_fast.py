# Uses python3
def calc_fib(n):
    f_num=[]
    f_num.append(int(0))
    f_num.append(int(1))
    for i in range(2:):
        f_num.append(int(f_num[i-1]+f_num[i-2]))
    return f_num[n-1]

n = int(input())
print(calc_fib(n))
