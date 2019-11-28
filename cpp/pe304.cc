#include <iostream>
#include <tuple>
#include <vector>

typedef long long unsigned int LL;
typedef std::tuple<LL, LL, LL, LL> M;

const LL MOD = 1234567891011llu;
const M I = std::make_tuple(1, 0, 0, 1);
const M F = std::make_tuple(1, 1, 1, 0);

M mul(const M& a, const M& b) {
  return std::make_tuple(
    ((std::get<0>(a)*std::get<0>(b))%MOD + (std::get<1>(a)*std::get<2>(b))%MOD)%MOD,
    ((std::get<0>(a)*std::get<1>(b))%MOD + (std::get<1>(a)*std::get<3>(b))%MOD)%MOD,
    ((std::get<2>(a)*std::get<0>(b))%MOD + (std::get<3>(a)*std::get<2>(b))%MOD)%MOD,
    ((std::get<2>(a)*std::get<1>(b))%MOD + (std::get<3>(a)*std::get<3>(b))%MOD)%MOD
  );
}

M p(const M& m, const LL n) {
  if (n == 0) return I;
  if (n == 1) return m;

  const M h = p(m, n / 2);
  const M q = mul(h, h);
  return mul(q, n % 2 == 1 ? m : I);
}

M pb(const M& m, LL n) {
  if (n == 0) return I;
  if (n == 1) return m;

  std::vector<LL> bs;
  while (n > 0) {
    bs.push_back(n);
    n /= 2;
  }

  std::vector<M> ps(bs.size(), F);
  for (int i = 1; i < ps.size(); ++i) {
    const M h = ps[i-1];
    const M q = mul(h, h);
    ps[i] = mul(q, bs[bs.size()-i-1] % 2 == 1 ? m : I);
  }
  return ps[ps.size()-1];
}

LL fib(const LL n) {
  const M x = pb(F, n);
  return std::get<1>(x);
}

int main() {
  std::cout << fib(1000000000000000llu) << std::endl;
}
