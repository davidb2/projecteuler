from math import lcm

var ans = 1
for i in 2..20:
  ans = lcm(ans, i)

echo ans