discard """
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

proc factors(num: int64): seq[int64] =
  var temp = num
  var ans: seq[int64] = @[]
  var d: int64 = 2
  while temp > 1:
    if temp mod d == 0:
      ans.add(d)
      temp = temp div d
    else:
      d += 1
  return ans

let fs = factors(600851475143)
let ans = fs[len(fs)-1]
echo ans