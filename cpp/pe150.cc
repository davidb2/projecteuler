#include <algorithm>
#include <climits>
#include <iostream>

constexpr int SIZE = 1000;
typedef long long int LL;
LL T[SIZE][SIZE];

void fillT() {
  for (int i = 0; i < SIZE; ++i) {
    for (int j = 0; j < SIZE; ++j) {
      T[i][j] = 0;
    }
  }
  int r = 0;
  LL t = 0;
  int k = 1;

  for (int n = 1; n <= SIZE; ++n) {
    for (int c = 0; c < n; ++c) {
      t = (615949*t + 797807) % (1 << 20);
      T[r][c] = t - (1 << 19);
      ++k;
    }
    ++r;
  }
}

int i(int r, int c, int s) {
  return s + (SIZE + 1) * (c + (SIZE + 1) * r);
}

int main() {
  fillT();

  LL* sumDown = new LL[(SIZE+1)*(SIZE+1)*(SIZE+1)];
  LL* sumTriangle = new LL[(SIZE+1)*(SIZE+1)*(SIZE+1)];
  for (int i = 0; i < (SIZE+1)*(SIZE+1)*(SIZE+1); ++i) {
    sumDown[i] = 0;
    sumTriangle[i] = 0;
  }

  LL ans = LLONG_MAX;
  for (int r = SIZE-1; r >= 0; --r) {
    for (int c = r; c >= 0; --c) {
      for (int s = 1; s <= SIZE; ++s) {
        sumDown[i(r, c, s)] = T[r][c] + sumDown[i(r+1, c, s-1)];
        sumTriangle[i(r, c, s)] = sumDown[i(r, c, s)] + sumTriangle[i(r+1, c+1, s-1)];
        ans = std::min(ans, sumTriangle[i(r, c, s)]);
      }
    }
  }

  std::cout << "Ans: " << ans << std::endl;

  delete[] sumDown;
  delete[] sumTriangle;
}
