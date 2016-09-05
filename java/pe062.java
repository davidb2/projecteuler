import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class pe062 {
	static HashMap<Integer, Long> f_cache = 
			new HashMap<Integer, Long>();
	static HashMap<Long, ArrayList<Integer>> hash_cache = 
			new HashMap<Long, ArrayList<Integer>>();
	public static void load_primes() {
		// So longs have numeric literals (L) but BigIntegers don't??
		// Java needs to allow coders to define literals
		// ANYWAYS, this maps a digit to a prime number.
		f_cache.put(0, 2L);
		f_cache.put(1, 3L);
		f_cache.put(2, 5L);
		f_cache.put(3, 7L);
		f_cache.put(4, 11L);
		f_cache.put(5, 13L);
		f_cache.put(6, 17L);
		f_cache.put(7, 19L);
		f_cache.put(8, 23L);
		f_cache.put(9, 29L);
	}
	// hash with multiplying primes
	// who knows, sorting the digits might have actually been quicker.
	// We are computing here a product of primes, thus only anagrams hash to each other
	public static long custom_hash(long number) {
		return Arrays.stream((number+"").split(""))
					.mapToLong(e -> f_cache.get(Integer.parseInt(e)))
					.reduce((prev_d, curr_d) -> prev_d * curr_d)
					.getAsLong();
	}
	public static void main(String[] args) {
		load_primes();
		int max_len = 0;
		long min_num = 0;
		for (long n = 0; max_len < 5; n++) {
			// we hash n's cube
			long hashed_n = custom_hash(n*n*n);
			if (!hash_cache.containsKey(hashed_n)) {
				hash_cache.put(hashed_n, new ArrayList<Integer>());
			}
			hash_cache.get(hashed_n).add((int)n);
			if (hash_cache.get(hashed_n).size() > max_len) {
				max_len = hash_cache.get(hashed_n).size();
				min_num = hash_cache.get(hashed_n).get(0);
			}
		}
		System.out.printf("%d^3 = %d is the smallest cube.", min_num, min_num*min_num*min_num);
	}
}
