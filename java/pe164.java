import java.util.HashMap;

public class pe164 {
	static HashMap<Byte, HashMap<Tuple, Long>> cache = 
			new HashMap<Byte, HashMap<Tuple, Long>>();
	public static long count(byte prev_digit, byte curr_digit, byte n) {
		// base case
		// how many numbers can we form 
		// if we are allowed to tack on 0 more digits to the end of the current number?
		// Well, just the current number.
		if (n == 0) {
			return 1;
		}
		// initialize inner cache
		if (!cache.containsKey(n)) {
			cache.put(n, new HashMap<Tuple, Long>());
		}
		Tuple t = new Tuple(prev_digit, curr_digit);
		// compute answer 
		if (!cache.get(n).containsKey(t)) {
			long ans = 0;
			// calculate possible next digits and their answers
			for (byte next_digit = 0; next_digit < 10-(prev_digit+curr_digit); next_digit++) {
				ans += count(curr_digit, next_digit, (byte)(n-1));
			}
			cache.get(n).put(t, ans);
		}
		return cache.get(n).get(t);
	}
	public static long ans(byte n) {
		if (n < 1) {
			return 0;
		} else if (n == 1) {
			return 9;
		} else if (n == 2) {
			return 45;
		} else {
			long num = 0;
			for (byte d1 = 1; d1 < 10; d1++) {
				for (byte d2 = 0; d2 < 10; d2++) {
					num += count(d1, d2, (byte)(n-2));
				}
			}
			return num;
		}
	}
	public static void main(String[] args) {
		System.out.printf("Answer: %d", ans((byte)20));
	}
}

// It would be nice if java supported tuples
public class Tuple {
	public byte a, b;
	private HashMap<Byte, Short> f_cache = 
			new HashMap<Byte, Short>();
	public Tuple(byte a, byte b) {
		this.a = a;
		this.b = b;
	}
	public Tuple(int a, int b) {
		this.a = (byte)a;
		this.b = (byte)b;
	}
	// I use this hashing function a lot because 
	// it is a constrained hashing function.
	// This means that if n or m were >= 29, 
	// There would start to be collisions.
	// Lucky for this problem, the max m or n is going
	// to be is 9 (because digits are 0 - 9).
	private int f(byte n, byte m) {
		if (!f_cache.containsKey(n)) {
			f_cache.put(n, (short)(2*n*n+29));
		}
		if (!f_cache.containsKey(m)) {
			f_cache.put(m, (short)(2*m*m+29));
		}
		return f_cache.get(n) * f_cache.get(m);
	}
	@Override
	public boolean equals(Object arg0) {
		// TODO Auto-generated method stub
		Tuple arg1 = (Tuple) arg0;
		return this.a == arg1.a && this.b == arg1.b;
	}
	@Override
	public int hashCode() {
		// TODO Auto-generated method stub
		return f(this.a, this.b);
	}
}