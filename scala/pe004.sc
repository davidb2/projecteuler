val nums = (100 to 999)
val an = (for (i <- nums) yield {
  for (j <- nums) yield {
    if (i <= j) (i, j)
  }
}).flatten.filter(x => x != ())

val ans = (for ((x: Int, y: Int) <- an) yield {
  x * y
})
  .filter(x =>
    x.toString()
      .equals(x.toString().reverse)
  ).max

print(ans)