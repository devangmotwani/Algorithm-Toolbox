import fibonacci
import fibonacci_fast
import random

if __name__=="__main__":
    n= random.randrange(15)
    a=[]
    while(True):
        #for i in range(n+1):
        #    a.append(random.randrange(10))
        #print(a)
        result1 = fibonacci.calc_fib(n)
        result2 = fibonacci_fast.fast_fib(n)

        if result1==result2:
            print ("OK")
        else:
            print("n="+str(n))
            print("fib= "+str(result1)+" fast_fib= "+str(result2) )
            break
