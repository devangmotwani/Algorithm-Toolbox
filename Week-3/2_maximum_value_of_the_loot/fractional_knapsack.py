# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    #print(capacity)
    #print(weights)
    #print(values)
    # write your code here
    x={}
    for i in range(len(values)):
        temp=float(values[i]/weights[i])
        x[temp]={}
        x[temp]['weight']=weights[i]
        x[temp]['value']=values[i]
    
    list_x=list(x.keys())
    (list_x.sort())
    #list_x=list_x[::-1]
    #print(list_x)
    #while(capacity>0 ):
    #for i in reversed(list_x):
    i=len(list_x)-1
    #print(i)
    while i>=0 and capacity>0:
        if x[list_x[i]]['weight']<=capacity:
            capacity-=x[list_x[i]]['weight']
            #print(value)
            value+=x[list_x[i]]['value']
        else:
            part=capacity
            capacity-=x[list_x[i]]['weight']
            value+=list_x[i]*part
        i=i-1

    #print(x)
    return value


if __name__ == "__main__":
    data = list(map(int, input().split()))#sys.stdin.read().split()))
    n, capacity = data[0:2]
    #values = data[2:(2 * n + 2):2]
    #weights = data[3:(2 * n + 2):2]
    values=[]
    weights=[]
    for i in range(n):
        v,w = map(int, input().split())
        values.append(v)
        weights.append(w)
    
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
