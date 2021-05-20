#include <algorithm>
#include <numeric>
#include <iostream>
#include <vector>

using std::vector;

typedef long long int LL;

LL S(size_t i) {
  return (i+1)*(i+1);
}
constexpr size_t SS = 100;
constexpr size_t C = 50;
constexpr size_t N = 295425;

short A[N+1][C+1];
short B[N+1][C+1];

void clear() {
  for (size_t n = 0; n <= N; n++) {
    for (size_t l = 0; l <= C; l++) {
      A[n][l] = 0;
      B[n][l] = 0;
    }
  }
}

LL solve() {
  clear();
  A[0][0] = 1;
  for (int i = SS-1; i >= 0; i--) {
    for (size_t n = 0; n <= N; n++) {
      for (size_t l = 0; l <= C; l++) {
        short a = 0;
        if (S(i)<=n && 1 <= l) {
          a = A[n-S(i)][l-1];
        }
        short b = A[n][l];
        B[n][l] = std::min(a+b, 2);
      }
    }
    std::swap(A, B);
  }

  LL sum = 0;
  for (size_t n = 0; n <= N; ++n) {
    if (A[n][C] == 1) {
      sum += n;
    }
  }
  return sum;
}

int main() {
  std::cout << solve() << std::endl;
}
