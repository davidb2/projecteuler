import java.math.BigInteger;
import java.util.HashMap;

public class pe076 {
	// creates a big integer (oh how java could use some numeric literals...)
	public static BigInteger b(int n) {
		return new BigInteger(n+"");
	}
	public static BigInteger answer(int n) {
		// just in case someone really doesn't know the answer
		if (n < 2) {
			return b(0);
		}
		
		// hold intermediate values
		HashMap<Integer, HashMap<Integer, BigInteger>> cache = 
				new HashMap<Integer, HashMap<Integer, BigInteger>>();
		cache.put(2, new HashMap<Integer, BigInteger>());
		// How many ways can we start with a number >= 1 
		// to list the partition in order of the number 2?
		// 1 + 1
		// 2
		// Answer: 2 ways, so inside of the 2's hashmap, key = 1, value = 2
		cache.get(2).put(1, b(2));
		// How many ways can we start with a number >= 2 
		// to list the partition in order of the number 2?
		// 2
		// Answer: 1 way, so inside of the 2's hashmap, key = 2, value = 1
		cache.get(2).put(2, b(1));
		// If the above wasn't clear, let's look at the number 4.
		// If we list all of 4's possible partitions in lexicographical order:
		// 1 + 1 + 1 + 1
		// 1 + 1 + 2
		// 1 + 3
		// 2 + 2
		// 4
		// This means that:
		// 		we can start with a number >= 1 and make 5 different partitions
		// 		we can start with a number >= 2 and make 2 different partitions
		// 		we can start with a number >= 3 and make 1 different partition
		// 		we can start with a number >= 4 and make 1 different partition
		// Using dynamic programming, 4's partitions will be but in the hashmap named "cache"
		// and in that cache, the answer is stored with the key = 1. But, Problem 76 stated that
		// a partition consists of the addition of two or more numbers, so we must subtract one 
		// from whatever answer we get.
		
		//////////////////////////////////////////////////////////////////////////////////////
		
		// we need to build up the answers
		// instead of doing literal recursion,
		// we can mimic recursion by building up answers.
		// This means we don't need to check if a value is in
		// the cache before accessing it; it is a guarantee.
		for (int np = 3; np <= n; np++) {
			// We know that there is only 1 way to make a partition of np that starts
			// with a number >= np, just np.
			cache.put(np, new HashMap<Integer, BigInteger>());
			cache.get(np).put(np, b(1));
			
			BigInteger sum = b(1);
			// Java needs to have operator overloading;
			// This is ridiculous.
			for (int nat_num = np/2; nat_num > 0; nat_num--) {
				// Here, we are getting the ways to partition a number 
				// BUT, all of the partitions must start with a number >= nat_num
				// For example, if np = 4 and nat_num = 1,
				// we are looking at 1 + 3.
				// Now, how many ways can I partition 3 such that 
				// the partition of 4 is still in order?
				// 1 + (1 + 1 + 1)
				// 1 + (1 + 2)
				// 1 + (3)
				// Answer: 3 ways
				// Another example, if np = 4 and nat_num = 2,
				// we are looking at 2 + 2.
				// Now, how many ways can I partition 2 such that 
				// the partition of 4 is still in order?
				// 2 + (2)
				// Answer: 2 ways
				// Notice that I didn't include 2 + (1 + 1) because
				// these numbers are not in ascending order. 
				// This code segment accounts for this
				// ALSO, we only have to look at numbers that are np/2 and below 
				// because if nat_num > np/2, the partition MUST be in non-ascending order,
				// thus invalid.
				sum = sum.add(cache.get(np-nat_num).get(nat_num));
			}
			for (int nat_num = 1; nat_num <= np/2; nat_num++) {
				// Gosling, operator overloading is needed in Java;
				// this is atrocious
				
				// Building the hashmap with the results we got above.
				cache.get(np).put(nat_num, sum);
				sum = sum.subtract(cache.get(np-nat_num).get(nat_num));
			}
			for (int nat_num = np/2 + 1; nat_num < np; nat_num++) {
				// As mentioned above, we know that partitions that 
				// start with a number > np/2 CANNOT POSSIBLY be in ascending order, 
				// well except for the single value partition of just np itself.
				cache.get(np).put(nat_num, b(1));
			}
		}
		// we are subtracting one because a valid partition consists
		// of the sum of two or more numbers, and one value inside of
		// cache[n][1] represents n itself as a partition, which is not a valid partition.
		return cache.get(n).get(1).subtract(b(1));
	}
	public static void main(String[] args) {
		int n = 100;
		System.out.printf("There are %s partitions of %d.", answer(n), n);
	}
	
	
	
	// same method as "answer" just w/out comments
	public static BigInteger answer_condensed(int n) {
		if (n < 2) {
			return b(0);
		}
		HashMap<Integer, HashMap<Integer, BigInteger>> cache = 
				new HashMap<Integer, HashMap<Integer, BigInteger>>();
		cache.put(2, new HashMap<Integer, BigInteger>());
		cache.get(2).put(1, b(2));
		cache.get(2).put(2, b(1));
		for (int np = 3; np <= n; np++) {
			cache.put(np, new HashMap<Integer, BigInteger>());
			cache.get(np).put(np, b(1));
			BigInteger sum = b(1);
			for (int nat_num = np/2; nat_num > 0; nat_num--) {
				sum = sum.add(cache.get(np-nat_num).get(nat_num));
			}
			for (int nat_num = 1; nat_num <= np/2; nat_num++) {
				cache.get(np).put(nat_num, sum);
				sum = sum.subtract(cache.get(np-nat_num).get(nat_num));
			}
			for (int nat_num = np/2 + 1; nat_num < np; nat_num++) {
				cache.get(np).put(nat_num, b(1));
			}
		}
		return cache.get(n).get(1).subtract(b(1));
	}
}