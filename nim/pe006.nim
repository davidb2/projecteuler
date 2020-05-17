import math

const LIM = 100
var ans: int = 0

for i in 1..LIM:
  ans -= i^2

var s: int = 0
for i in 1..LIM:
  s += i
ans += s^2

echo ans