# def sod(n):
#    divisors = []
#    temp_divisors = []
#    divisors.append(1)
#    temp_divisors.append(1)
#    for i in range(2,int(n**0.5)+1):
#        if n % i == 0:
#            divisors.append(i)
#            temp_divisors.append(i)
#    for i in reversed(temp_divisors[1:len(temp_divisors)]):
#        divisors.append(int(n/i))
#    return sum(list(set(divisors)))
# def abundant(n):
#    return sod(n) > n
# ab = list(filter(abundant, list(range(12, 28124))))
# sums_of_ab = []
# for i in ab:
#    for j in ab:
#        if i+j > 28123:
#            break
#        else:
#            sums_of_ab.append(i+j)
# sums_of_ab = set(sums_of_ab)
# sums = {key: True for key in range(28124)}
# for i in sums_of_ab:
#    sums[i] = False
# ans = 0
# for i in range(28124):
#    if sums[i]:
#        ans += i
# print(ans)

# optimized version

LIMIT = 28123
abundant_nums = []
abundant_sums = set()
def sieve():
    ps = [0 for _ in xrange(LIMIT+1)]
    for step in xrange(1, LIMIT//2+1):
        for p in xrange(2*step, LIMIT+1, step):
            ps[p] += step
    for n in xrange(LIMIT+1):
        if ps[n] > n:
            abundant_nums.append(n)

sieve()
for i in xrange(len(abundant_nums)):
    for j in xrange(i, len(abundant_nums)):
        k = abundant_nums[i] + abundant_nums[j]
        if k > LIMIT:
            break
        else:
            abundant_sums.add(k)
ans = ((LIMIT)*(LIMIT+1))//2 - sum(abundant_sums)
print ans