var ans = 0

var a = 2
var b = 1

while a <= 4_000_000:
  if a mod 2 == 0:
    ans += a

  let temp = a
  a = a+b
  b = temp

echo ans