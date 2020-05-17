var ans: int = 0

for i in 0..<1000:
  if i mod 3 == 0 or i mod 5 == 0:
    ans += i

echo ans