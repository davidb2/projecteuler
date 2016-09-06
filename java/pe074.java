import java.util.Arrays;
import java.util.HashMap;

public class NOTOPTIMIZEDProblem74 {
	static HashMap<Long, Integer> cache = new HashMap<Long, Integer>();
	static HashMap<Integer, Long> fact_cache = new HashMap<Integer, Long>();
	public static long factorial(int n) {
		if (!fact_cache.containsKey(n)) {
			// this is not tail recursive, 
			// but we will only need to compute 9! at most one time
			// no harm done
			fact_cache.put(n, n * factorial(n-1));
		}
		return fact_cache.get(n);
	}
	// we will define a number's hash as the sum of the factorial of the digits
	public static long custom_hash(long n) {
		return Arrays.stream((n+"").split(""))
				.mapToLong(e -> factorial(Integer.parseInt(e)))
				.sum();
	}
	public static int compute_chain(long n) {
		HashMap<Long, Boolean> local_cache = new HashMap<Long, Boolean>();
		int acc = 0;
		while (true) {
			// System.out.print(n + " -> ");
			if (cache.containsKey(n)) 
			if (!local_cache.containsKey(n)) {
				local_cache.put(n, true);
				acc++;
			}
			else {
				break;
			}
			n = custom_hash(n);
		}
		// System.out.println();
		return acc;
	}
	public static void main(String[] args) {
		fact_cache.put(0, 1L);
		int answer = 0;
		for (int n = 0; n < 1000000; n++) {
			if (compute_chain(n) == 60) {
				answer++;
			}
		}
		System.out.printf("Answer: %d", answer);
	}
}
