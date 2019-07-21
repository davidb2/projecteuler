MOD = 1000000


if __name__ == '__main__':
  # Just a guess. 10^10 operations.
  n = int(10 ** (10 / 2.))

  S = [1] + [0]*n
  for j in range(1, n+1):
    for i in range(j, n+1):
      S[i] = (S[i] + S[i-j]) % MOD
    if S[j] == 0:
      print(j)
      break