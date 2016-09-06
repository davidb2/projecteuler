import java.util.HashMap;
class pe178 {
    static int[] f = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    static final long magic_num = 6469693230L;
    static HashMap<Long[], Long> cache = new HashMap<Long[], Long>();
    static long ways(int d, int n, long acc) {
        if (n == 0) {
            return acc == 0 ? 1 : 0;
        }
        Long[] key = {Long.valueOf(d), Long.valueOf(n), acc};
        if (!cache.containsKey(key)) {
            long smaller = d-1 >= 0 ? ways(d-1, n-1, (acc * f[d-1]) % magic_num) : 0;
            long bigger = d+1 < 10 ? ways(d+1, n-1, (acc * f[d+1]) % magic_num) : 0;
            cache.put(key, smaller + bigger);
        }
        return cache.get(key);
    }
    public static void main(String[] args) {
        long ans = 0;
        for (int n = 2; n < 41; n++) {
            for (int d = 1; d < 10; d++) {
                ans += ways(d, n-1, f[d]);
            }
        }
        System.out.println(ans);
    }
}