#include <iostream>
#include <unordered_map>

typedef long long int LL;

int collatz(const LL n, std::unordered_map<LL, int>& cache) {
  if (n == 1) return 1;
  if (cache.find(n) == cache.end()) {
    if (n % 2 == 0) {
      cache[n] = 1 + collatz(n/2, cache);
    } else {
      cache[n] = 1 + collatz(3*n+1, cache);
    }
  }
  return cache[n];
}

int main() {
  std::unordered_map<LL, int> cache;
  LL m = 0;
  int mn = 0;

  for (LL n = 1; n < 1000000; ++n) {
    int ans = collatz(n, cache);
    if (ans > mn) {
      m = n;
      mn = ans;
    }
  }

  std::cout << m << " " << mn << std::endl;
}
