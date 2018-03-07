# Uses python3
import sys

def fibonacci_sum(n):
    if n <= 1:
        return n

    #previous = 0
    #current  = 1
    #sum      = 1
    """
    # Sum of n Fibonacci numbers = F(n+2) - 1
    # So find the F(n+2 ofcourse not naively)
    # Units place digit repeats after every 60 fibonacci numbers
    # A buffer is created to save the unit digits of the numbers 
    # Take modulo of the number you obtain and call the value from the buffer and return it 
    after subtracting 1 from it
    """ 
    buffer=fast_fib(59)
    #print("Length=",len(buffer))
    #print(buffer,end="\t")
    if (n+2)>=60:
        value=int((n+2)%60)
        #print("\nValue= "+str(value))
        #value=value-1
        #print("Buffer= "+str(buffer[value]))
        if buffer[value]==0:
            return 9            # To avoid 0-1 resulting in -1 as it is actually 9
        return buffer[value]-1
    else:
        temp=n+2
        if buffer[temp]==0:
            return 9
        return buffer[temp]-1
    #sum = fast_fib(n+2) - 1
    #return sum % 10

def fast_fib(n):
    if n<=1:
        return n
    f_num=[]
    f_num.append(int(0))
    f_num.append(int(1))
    for i in range(2,n+1):
        temp= int(f_num[-1]%10+f_num[-2]%10)
        f_num.append(int(temp%10))
    #for i in f_num:
    #    print (i)
    return f_num

if __name__ == '__main__':
    input_cmd = input() #sys.stdin.read()
    n = int(input_cmd)
    print(fibonacci_sum(n))
