from math import ceil, sqrt
primes = set([3])
not_primes = set()


def is_prime(n):
  if n in primes or n in not_primes:
    return n in primes
  for d in xrange(3, int(sqrt(n) + 1)):
    if n % d == 0:
      not_primes.add(n)
      return False
  primes.add(n)
  return True


n = 5
while True:
  solution = False
  for x in xrange(int(sqrt(n) / sqrt(2)), -1, -1):
    pp = n - 2 * x**2
    if is_prime(pp):
      # for debugging
      # print '{} = {} + 2 * {} ** 2'.format(n, pp, x)
      solution = True
      break
  if not solution:
    print n
    break
  n += 2