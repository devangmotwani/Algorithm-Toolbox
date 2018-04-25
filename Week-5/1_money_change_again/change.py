# Uses python3
import sys

def get_change(m,dens):
    if m in dens:
        return 1
    min_change=[]
    min_change.append(0)
    min_change.append(1)
    min_change.append(2)
    min_change.append(1)
    min_change.append(1)
    if m==2:
        return 2
    i=5
    while(i<=m):
        a=1
        b=i-1
        temp=[]
        while a<=b:
            if a==b:
                temp.append(min_change[a]*2)
            else:
                temp.append(min_change[a]+min_change[b])
            a+=1
            b-=1
        min_change.append(min(temp))
        #print((temp))
        i+=1
        #print("change",min_change)
    return min_change[-1]

if __name__ == '__main__':
    m = int(input())#int(sys.stdin.read())
    dens=[1,3,4]
    changes=get_change(m,dens)
    print(changes)
