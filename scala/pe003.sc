def isPrime(n: Long): Boolean = {
  val limit: Long = math.sqrt(n).toLong+1
  def ip(np: Long, i: Long, lim: Long): Boolean = {
    if (i > lim) {
      true
    } else {
      np%i != 0 && ip(np, i+2, lim)
    }
  }
  n > 1 && ((n == 2) || (n % 2 != 0 && ip(n, 3, limit)))
}

def largestPrimeFactors(n: Long): Long = {
  def pf(np: Long, i: Long): Long = {
    if (np == i) {
      np
    } else if (!isPrime(i)) {
      pf(np, i+2)
    } else if (np % i == 0) {
      pf(np/i, i)
    } else {
      pf(np, i + (if (i==2) 1 else 2))
    }
  }
  pf(n, 2)
}
val ans = largestPrimeFactors(600851475143L)
println(ans)