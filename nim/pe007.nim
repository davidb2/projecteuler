proc nthPrime(n: int): int =
  var ans: seq[int] = @[2]

  var x = 3
  while len(ans) < n:

    var isPrime = true
    for a in ans:
      if x mod a == 0:
        isPrime = false
        break

    if isPrime:
      ans.add(x)

    x += 2

  return ans[len(ans)-1]

echo nthPrime(10001)