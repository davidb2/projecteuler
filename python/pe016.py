def sod(n):
    return sum(list(map(int, list(str(n)))))
ans = sod(2**1000)
print(ans)