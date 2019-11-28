#include <cmath>
#include <iostream>
#include <map>
#include <tuple>

typedef long long int LL;

std::map<std::tuple<LL, int, int>, LL> cache;

LL W(LL n, int i, int t) {
  if (t > 2 || n < 0) return 0;
  if (n == 0) return 1;

  const auto x = std::make_tuple(n, i, t);
  if (cache.find(x) == cache.end()) {
    LL p = pow(2, i);
    cache[x] = W(n-p, i, t+1) + (n >= 2*p ? W(n, i+1, 0) : 0);
  }
  return cache[x];
}

int main() {
  LL N = pow(10, 8);
  LL ans = W(N, 0, 0);
  std::cout << ans << std::endl;
}
