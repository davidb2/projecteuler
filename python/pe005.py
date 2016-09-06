def is_divisible(n):
    for i in range(1,21):
        if n % i != 0:
            return False
    return True
ans = 20
while not is_divisible(ans):
    ans += 20
print(ans)