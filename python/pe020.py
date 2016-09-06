def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f
def sod(n):
    return sum(list(map(int, list(str(n)))))
ans = sod(fact(100))
print(ans)

# or 

from functools import reduce
print(sum(map(int,str(reduce(lambda x,y:x*y,range(1, 101),1)))))