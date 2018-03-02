# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

#print(a)
max_number=max(a)
max_index=a.index(max_number)
a.pop(max_index)
max_number2=max(a)
result=max_number*max_number2
print(result)
