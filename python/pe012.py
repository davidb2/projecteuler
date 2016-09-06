def t(n):
    return int((n**2 + n)/2)
def d(n):
    divisors = []
    temp_divisors = []
    divisors.append(1)
    temp_divisors.append(1)
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            temp_divisors.append(i)
    for i in reversed(temp_divisors):
        divisors.append(int(n/i))
    return divisors
i = 1
while len(d(t(i))) <= 500:
    i += 1
ans = t(i)
print(ans)