# Uses python3
import sys

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n
    
    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current%10 , ((previous%10 + current%10)%10)
        print (current)
    return current

if __name__ == '__main__':
    input_cmd = input()#sys.stdin.read()
    n = int(input_cmd)
    print(get_fibonacci_last_digit(n))
