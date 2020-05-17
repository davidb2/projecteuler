import math
import strutils
import unicode

proc pals(d: int): seq[int] =
  var ans: seq[int] = @[]

  for a in 10^(d-1)..<10^d:
    for b in a..<10^d:
      let c = a*b
      let d = intToStr(c)
      if d == reversed(d):
        ans.add(c)

  return ans


var ans = max(pals(3))
echo ans