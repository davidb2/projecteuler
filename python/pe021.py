# def sod(n):
#    divisors = []
#    temp_divisors = []
#    divisors.append(1)
#    temp_divisors.append(1)
#    for i in range(2,int(n**0.5)+1):
#        if n % i == 0:
#            divisors.append(i)
#            temp_divisors.append(i)
#    for i in reversed(temp_divisors):
#        divisors.append(int(n/i))
#    divisors.pop(len(divisors)-1)
#    return sum(divisors)
# def is_amicable(n):
#    b = sod(n)
#    a = sod(b)
#    if a != b and a == n:
#        return True
#    else:
#        return False
# ans = sum(list(filter(is_amicable, list(range(1,10000)))))
# print(ans)

LIMIT = 10000
def sieve():
    ps = [0 for _ in xrange(LIMIT)]
    for step in xrange(1, LIMIT//2):
        for p in xrange(2*step, LIMIT, step):
            ps[p] += step
    return ps

ps = sieve()
ans = 0
for x in xrange(LIMIT):
    try:
        if ps[ps[x]] == x and x != ps[x]:
            ans += x
    except:
        pass # lol
print ans