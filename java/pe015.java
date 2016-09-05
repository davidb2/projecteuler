import java.util.HashMap;

public class pe015 {
	static HashMap<Long, Long> cache = new HashMap<Long, Long>();
	static HashMap<Integer, Long> f_cache = new HashMap<Integer, Long>();
	// hashing function => f(n, m) = (2n^2 + 29) * (2m^2 + 29) 
	// Storing int[] in a hashmap didn't work well
	public static Long f(int n, int m) {
		if (!f_cache.containsKey(n)) {
			f_cache.put(n, 2*n*n+29L);
		}
		if (!f_cache.containsKey(m)) {
			f_cache.put(m, 2*m*m+29L);
		}
		return f_cache.get(n) * f_cache.get(m);
	}
	public static Long ways(int n, int m) {
		if (n == 0 || m == 0) {
			return 1L;
		}
		if (!cache.containsKey(f(n, m))) {
			// recurrence relation
			cache.put(f(n, m), ways(n, m-1) + ways(n-1, m));
		}
		return cache.get(f(n, m));
	}
	public static void main(String[] args) {
		// a 1x1 has only two ways
		cache.put(f(1, 1), 2L);
		long answer = ways(20, 20);
		System.out.printf("Answer: %d", answer);
	}
}
