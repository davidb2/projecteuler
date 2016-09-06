from functools import reduce
num = open('../pe008.txt').read().replace('\n', '')
grid = list(map(int, num))
products = []
for i in range(1000-13+1):
    product = reduce(lambda x, y: x * y, grid[i:i+13])
    products.append(product)
ans = max(products)
print(ans)