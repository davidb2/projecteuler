MAX = 10000
MAXS = MAX**2
squares = list(map(lambda x: x**2, range(1, MAX)))


def is_palindrome(n):
    np = str(n)
    return np == ''.join(reversed(np))

cache = {}
total = 0
for x in range(MAX-1):
    y = x+1
    temp = squares[x]
    while temp < MAXS:
        if y-x > 1 and temp not in cache and is_palindrome(temp):
            # print(' + '.join(map(str, squares[x:y])), '=', temp)
            total += temp
            cache[temp] = True
        try:
            temp += squares[y]
            y += 1
        except:
            break
print(total)