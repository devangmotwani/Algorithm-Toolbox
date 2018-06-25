# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right <= left:
        #print ("Single element",a[right])
        #return
        return number_of_inversions
    #print("left=",left)
    #print("right=",right)
    mid = (left + right) // 2
    
    number_of_inversions += get_number_of_inversions(a,mid-left+1,left,mid)
    number_of_inversions += get_number_of_inversions(a,right-(mid+1)+1,mid+1,right)
    
    #number_of_inversions += get_number_of_inversions(a, b, left, ave)
    #number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    number_of_inversions += merge(a,right-left+1,left,mid+1)
    return number_of_inversions

def merge(a,length_a,p1,p2):
    number=0
    start=p1
    mid=p2-1
    temp=[]
    #print("p1=",p1)
    #print("p2=",p2)
    #print("length_a=",length_a)
    while p1<=mid and p2<(start+length_a):
        if a[p1]>a[p2]:
            temp.append(a[p2])
            p2+=1
            number += (mid-p1)+1 
        else:
            temp.append(a[p1])
            p1+=1
    #print("Before",temp) 
    while p1<mid+1:
        temp.append(a[p1])
        #print("p1 ",temp)
        p1+=1
    while p2<length_a:
        temp.append(a[p2])
        p2+=1

    #print("temp ",temp)
    for i in range(len(temp)):
        a[start+i]=temp[i]

    #print("modified a=",a)
    return number


if __name__ == '__main__':
    input_cmd = input() #sys.stdin.read()
    input_cmd2=input()
    n= (map(int, input_cmd.split()))
    a= list(map(int, input_cmd2.split()))
    b = n

    #n, *a = list(map(int, input.split()))
    #b = n * [0]
    number = int(get_number_of_inversions(a, b, 0, len(a)-1))
    #print(a)
    print(number)
    #get_number_of_inversions(a,b,0,len(a)-1)
    #print(a)
