# Uses python3
import sys
#import gcd_fast

def gcd(a, b):
    if (b==0):
        return a
    a_bar = a%b
    #print (a_bar)
    return gcd(b,a_bar)

def lcm(a, b):
    gcd_value=gcd(a,b)
    return int(int(a/gcd_value)*(int(b))) 

if __name__ == '__main__':
    input_cmd = input()#sys.stdin.read()
    a, b = map(int, input_cmd.split())
    print(lcm(a, b))

