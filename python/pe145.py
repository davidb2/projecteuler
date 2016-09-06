cache = {}
def is_reversible(n):
    # if n in cache: return cache[n]
    a = str(n)
    b = str(n)[::-1]
    if n%10 == 0 or int(a[0])%2 == int(a[-1])%2: 
        # cache[int(b)] = False
        return False
    carry = 0
    for i in range(len(a)):
        s = int(a[i]) + int(b[i]) + carry
        if s % 2 == 0:
            # cache[int(b)] = False
            return False
        carry = s//10
    # cache[int(b)] = True
    return True

s = 0
for j in range(9):
    for i in range(int(10**(j-1)), int(10**j)):
        s += int(is_reversible(i))
    # debugging purposes
    print(s)
print(s)