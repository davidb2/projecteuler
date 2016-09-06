# top down approach
cache = [
    [0],
    [0] + [1]
]
# swal = starts with at least
def calculate(n):
    if cache[n] == []:
        cache[n] = [0] + [1 for i in range(n)]
        acc = 1
        for swal in reversed(range(1, n//2+1)):
            remainder = n - swal 
            if cache[remainder] == []:
                calculate(remainder)
            cache[n][swal] = cache[remainder][swal] + acc
            acc += cache[remainder][swal]
def partitions(n):
    for i in range(2, n+1):
        cache.append([])
    calculate(n)
    return cache[n][1]-1
    
print(partitions(100))