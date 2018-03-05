# Uses python3
import sys

def gcd(a, b):
    if (b==0):
        return a
    a_bar = a%b
    #print (a_bar)
    return gcd(b,a_bar)

if __name__ == "__main__":
    input_cmd = input() #sys.stdin.read()
    a, b = map(int, input_cmd.split())
    print(gcd(a, b))
