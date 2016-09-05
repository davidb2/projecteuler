import java.util.HashMap;

public class pe113 {
	// We can use bytes because a digit is only 0 - 9
	// and the number of digits in 1e100 < 2^7
	// just saving some space
	static HashMap<Byte, HashMap<Byte, Long>> increasing_cache = 
			new HashMap<Byte, HashMap<Byte, Long>>();
	static HashMap<Byte, HashMap<Byte, Long>> decreasing_cache = 
			new HashMap<Byte, HashMap<Byte, Long>>();
	public static long inc(byte digit, byte n) {
		// base case
		// how many numbers can we form 
		// if we are allowed to tack on 0 more digits to the end of the current number?
		// Well, just the current number.
		if (n == 0) {
			return 1;
		}
		// initialize inner cache
		if (!increasing_cache.containsKey(n)) {
			increasing_cache.put(n, new HashMap<Byte, Long>());
		}
		// compute answer 
		if (!increasing_cache.get(n).containsKey(digit)) {
			long ans = 0;
			// calculate possible next digits and their answers
			for (byte x = digit; x < 10; x++) {
				ans += inc(x, (byte)(n-1));
			}
			increasing_cache.get(n).put(digit, ans);
		}
		return increasing_cache.get(n).get(digit);
	}
	public static long dec(byte digit, byte n) {
		// base case
		// how many numbers can we form 
		// if we are allowed to tack on 0 more digits to the end of the current number?
		// Well, just the current number.
		if (n == 0) {
			return 1;
		}
		// initialize inner cache
		if (!decreasing_cache.containsKey(n)) {
			decreasing_cache.put(n, new HashMap<Byte, Long>());
		}
		// compute answer 
		if (!decreasing_cache.get(n).containsKey(digit)) {
			long ans = 0;
			// calculate possible next digits and their answers
			for (byte x = digit; x >= 0; x--) {
				ans += dec(x, (byte)(n-1));
			}
			decreasing_cache.get(n).put(digit, ans);
		}
		return decreasing_cache.get(n).get(digit);
	}
	static final byte MAX_DIGITS = 100;
	public static void main(String[] args) {
		long ans = 0;
		// compute the answer
		for (byte num_of_digits = 0; num_of_digits < MAX_DIGITS; num_of_digits++) {
			// number mustn't start with a 0
			for (byte digit = 1; digit < 10; digit++) {
				ans += inc(digit, (byte)(num_of_digits)) + dec(digit, num_of_digits);
			}
			// remove duplicates (ie. 5555, 99999)
			// we are removing numbers that are not:
			//		increasing, decreasing, are bouncy
			ans -= 9; 
		}
		System.out.printf("Answer: %d", ans);
	}
}
