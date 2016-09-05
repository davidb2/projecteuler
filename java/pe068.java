import java.util.ArrayList;
import java.util.stream.IntStream;

// here is a good example of functional programming 
// (there are better ways to solve this problem though)
// but this program runs fast enough (~3 seconds)
public class pe068 {
	/*
	 * 		a
			 \  
			  x
			 / \
		    z - y - b
		   /	   
		  c	 
		  
		  magic 3-gon ring
		  
		  a x y
		  b y z
		  c z x
		  
		  This can be scaled to a magic 5-gon ring.
		  
		  For a 3-gon ring, it is possible to get a total of 9 through 12.
		  Why?
		  the lowest possible pair of three is 6, 1, 2
		  and the highest possible pair of three is 6, 5, 1
		  
		  So, for a 5-gon ring,
		  the lowest possible pair of three is 10, 1, 2
		  and the highest possible pair of three is 10, 9, 1
	 */
	public static int[] removeAt(int[] a, int i) {
		int[] b = new int[a.length-1];
		for (int x = 0; x < i; x++) {
			b[x] = a[x];
		}
		for (int x = i+1; x < a.length; x++) {
			b[x-1] = a[x];
		}
		return b;
	}
	static ArrayList<int[]> perms = new ArrayList<int[]>();
	public static void perm_helper(int[] p, int[] a, int i, int n) {
		if (i == n) {
			perms.add(p);
		} else {
			for (int x = 0; x < a.length; x++) {
				int[] pn = new int[p.length];
				for (int y = 0; y < p.length; y++) {
					pn[y] = p[y];
				}
				pn[i] = a[x];
				int[] b = removeAt(a, x);
				perm_helper(pn, b, i+1, n);
			}
		}
	}
	public static ArrayList<int[]> all_permutations(int n) {
		perm_helper(new int[n], IntStream.rangeClosed(1, n).toArray(), 0, n);
		return perms;
	}
	public static int min(ArrayList<Integer> arr) {
		int min = Integer.MAX_VALUE;
		for (int e : arr) {
			if (e < min) {
				min = e;
			}
		}
		return min;
	}
	public static String str(int n) {
		return n+"";
	}
	public static String ways(ArrayList<Integer> alpha, ArrayList<Integer> omega, int prev_sum, String acc) {
		if (alpha.isEmpty()) {
			return new StringBuilder(acc).reverse().toString();
		} else {
			int x = alpha.remove(0);
			int y = omega.remove(0);
			int yp = omega.get(0);
			if (x+y+yp == prev_sum) {
				return ways(alpha, omega, prev_sum, str(yp) + str(y) + str(x) + acc);
			} else if (prev_sum < 0 && x <= Math.abs(prev_sum)/2+1 && x < min(alpha)) {
				int new_sum = x+y+yp;
				omega.add(y);
				return ways(alpha, omega, new_sum, str(yp) + str(y) + str(x) + acc);
			} else {
				return "";
			}
		}
	}
	public static String compute(int[] a) {
		ArrayList<Integer> fst = new ArrayList<Integer>();
		ArrayList<Integer> snd = new ArrayList<Integer>();
		for (int i = 0; i < a.length/2; i++) {
			fst.add(a[i]);
			snd.add(a[i+a.length/2]);
		}
		return ways(fst, snd, -a.length, "");
	}
	public static void main(String[] args) {
		int n = 5;
		ArrayList<int[]> p = all_permutations(2 * n);
		String answer = 
				p.stream()
					.map(arr -> compute((int[])arr))
					.filter(s -> !s.equals(""))
					.max(String::compareTo)
					.get();
		System.out.printf("Answer: %s", answer);
	}
}