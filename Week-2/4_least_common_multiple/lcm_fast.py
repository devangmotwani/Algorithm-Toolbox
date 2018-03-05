# Uses python3
import sys
import gcd_fast

def lcm(a, b):
    gcd=gcd_fast.gcd(a,b)
    return int(int(a/gcd)*(int(b)))

if __name__ == '__main__':
    input_cmd = input()#sys.stdin.read()
    a, b = map(int, input_cmd.split())
    print(lcm(a, b))

