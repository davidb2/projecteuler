ans = 0
for a in range(1,999):
    for b in range(1,999):
        if a + b > 999:
            break
        c = 1000 - (a + b)
        if a + b + c == 1000 and a**2 + b**2 == c**2:
            ans = a*b*c
            break
    if ans != 0:
        break
print(ans)