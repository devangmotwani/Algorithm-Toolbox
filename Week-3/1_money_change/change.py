# Uses python3
import sys

def get_change(m):
    #write your code here
    tens=int(m/10)
    temp=float(m%10)
    fives=int(temp/5)
    ones=float(temp%5)
    return tens+fives+int(ones)

if __name__ == '__main__':
    m = int(input())#sys.stdin.read())
    print(get_change(m))
