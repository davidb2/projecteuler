def dbsosqasqos(n):   
    a = list(range(1,n+1))
    def sqos(ns):
        return sum(ns)**2
    def sosq(ns):
        return sum(list(map(lambda x: x**2, ns)))
    return sqos(a) - sosq(a)
ans = dbsosqasqos(100)
print(ans)