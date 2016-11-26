#include <cstdio>

const long LIMIT = 1 << 30;

int cw(long a, long b, long c) {
    return (a^b^c)==0;
}

int main() {
    int ans = 0;
    for (long n = 1; n <= LIMIT; n++) {
        ans += cw(n, 2L*n, 3L*n);
    }
    printf("%d\n", ans);
    return 0;
}