nums = list(map(int, open('../pe013.txt').read().split('\n')))
ans = str(sum(nums))[0:10]
print(ans)