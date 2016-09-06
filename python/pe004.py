def is_palindrome(n):
    return list(str(n)) == list(reversed(str(n)))
products = []
for i in range(100,1000):
    for j in range(100,1000):
        product = i * j
        if is_palindrome(product):
            products.append(product)
ans = max(products)
print(ans)