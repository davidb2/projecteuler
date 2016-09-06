from functools import reduce
products = []
grid = list(map(lambda x: list(map(lambda y: int(y), x.split(' '))), open('../pe011.txt').read().split('\n')))
def h():
    for i in range(20):
        for j in range(20-4+1):
            product = reduce(lambda x, y: x * y, grid[i][j:j+4])
            products.append(product)
def v():
    for j in range(20):
        for i in range(20-4+1):
            product = reduce(lambda x, y: x * y, [grid[i][j], grid[i+1][j], grid[i+2][j], grid[i+3][j]])
            products.append(product)
def dn():
    for i in range(16+1):
        for j in range(16+1):
            product = reduce(lambda x, y: x * y, [grid[i][j], grid[i+1][j+1], grid[i+2][j+2], grid[i+3][j+3]])
            products.append(product)
def dp():
    for i in reversed(range(3,20)):
        for j in range(16+1):
            product = reduce(lambda x, y: x * y, [grid[i][j], grid[i-1][j+1], grid[i-2][j+2], grid[i-3][j+3]])
            products.append(product)
def lping():
    h()
    v()
    dn()
    dp()
    return max(products)
ans = lping()
print(ans)