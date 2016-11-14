val LIMIT: Int = 4000000
def evenFibs(a: Int, b: Int, acc: Int): Int = {
  if (b > LIMIT) {
    acc
  } else {
    evenFibs(b, a+b, acc+(if (b%2==0) b else 0))
  }
}

val ans = evenFibs(0, 1, 0)
println(ans)