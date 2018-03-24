import bs
from random import *

if __name__ == '__main__':
    cap=randint(10,20)
    a=[]
    x=[]
    for i in range(cap):
        a.append(randint(1,20))
    a.sort()
    for i in range(15):
        x.append(randint(1,30))
    left=0
    right=len(a)

    for i in x:
        print("a",a)
        print("x",i)
        print(bs.binary_search(a,i),end=' ')
        print("\n")
