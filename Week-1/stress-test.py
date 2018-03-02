# Uses python3
import random

#n = int(input())
#a = [int(x) for x in input().split()]
#assert(len(a) == n)

def max_product(a):
    result = 0
    max_number=max(a)
    max_index=a.index(max_number)
    a.pop(max_index)
    max_number2=max(a)
    result=max_number*max_number2
    return result



def max_pair(a):
    result = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]

    return result

if __name__=="__main__":
    n= random.randrange(9)
    a=[]
    while(True):
        for i in range(n+1):
            a.append(random.randrange(10))
        print(a)
        result1 = max_product(a)
        result2 = max_pair(a)

        if result1==result2:
            print ("OK")
        else:
            print("max_pro= "+str(result1)+"max_pair= "+str(result2) )
            break

