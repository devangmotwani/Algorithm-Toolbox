# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    count={}
    for i in range(left,right):
        if a[i] in count:
            count[a[i]]+=1
        else:
            count[a[i]]=1
    max_count=(list(count.values()))
    #print(max_count)
    m_count=max(max_count)
    if m_count> ((right+left)/2):
        return 1
    else:
        return -1

if __name__ == '__main__':
    input_cmd = input()#sys.stdin.read()
    input_cmd2 = input()
    n = list(map(int, input_cmd.split())) 
    n=n.pop()
    a = list(map(int, input_cmd2.split()))
    #print(n)
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
