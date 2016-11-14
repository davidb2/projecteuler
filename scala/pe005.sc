def gcd(a: Long, b: Long): Long = {
  if (b == 0) a else gcd(b, a%b)
}
def lcm(a: Long, b: Long): Long = {
  (a * b) / gcd(a, b)
}
val ans = (1L to 20L).reduce((x, y) => lcm(x, y))

println(ans)