from collections import deque
from itertools import count
from decimal import Decimal, getcontext

getcontext().prec = 30

def get_tau(theta: Decimal, n: int) -> str:
  a, b = int(theta), theta
  ts = []
  for _ in range(n):
    b = a*(1+b-a)
    a = int(b)
    ts.append(str(a))
  return f"{int(theta)}.{''.join(ts)}"


thetas = deque()
thetas.append(("2.", 0))

while thetas:
  theta, n = thetas.popleft()
  tau = get_tau(Decimal(theta), n)
  print(f"{theta=}, {tau=}")
  if not tau.startswith(theta): continue
  if n >= 24:
    print(theta, tau, n)
    break
  for d in range(10):
    thetas.append((f"{theta}{d}", n+1))
