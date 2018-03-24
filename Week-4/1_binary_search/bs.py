# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1
    # write your code here
    #if right<left:
    #    return left-1
    if x<a[left] or x>a[right] or right<left:
        return -1
    return bs(a,left,right,x)

def bs(a,left,right,x):
    mid=int((right+left)/2)
    if mid==right and mid==left:
        if a[mid]==x:
            return left
        else:
            return int(-1)
    if a[mid]==x:
        return mid
    elif x>a[mid]: 
        #print ("x is Greater",mid+1,right)
        if x<a[mid+1]:
            return -1
        return bs(a,mid+1,right,x)
    elif x<a[mid]:
        #print("x is smaller",left,mid-1)
        if x>a[mid-1]:
            return -1
        return bs(a,left,mid-1,x)
    else:
        return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input_cmd1 = input()#sys.stdin.read()
    input_cmd2 = input()
    data = list(map(int, input_cmd1.split()))
    key = list(map(int,input_cmd2.split()))
    n = data[0]
    m = key[1:]
    a = data[1 :]
    left=0
    right=len(a)-1
    #print(len(a), right)
    for x in m:
        # replace with the call to binary_search when implemented
        print(binary_search(a,x), end = ' ')
        #print(x,)
    #print(bs(a,left,right,5), end = ' ')
        
