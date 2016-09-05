import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
// just add the maximum of the two parents as you traverse down
// dynamic programming
// also a lot of functional programming
// also a solution for problem 18
public class pe067 {
	public static int[] toTriangle(String numbers) {
		return
				Arrays.stream(
						numbers
							.replaceAll("\\s+", " ")
							.trim()
							.split(" "))
				.mapToInt(Integer::parseInt).toArray();		
	}
	// Ah, loosely switching types
	// When I wrote this program in F#, 
	// it tracked all of my type conversions beautifully!
	// Ah, Java...
	// The Java compiler (javac) is giving us warnings because
	// in the below method, I am changing the type from String[] to int[],
	// and the compiler is not catching that.
	@SuppressWarnings("unchecked")
	public static ArrayList<Object> read(String filepath) {
		Path path = Paths.get(filepath);
		try {
			return
					new ArrayList(Arrays.asList(Files
								.lines(path)
								.map(s -> toTriangle(s))
								.toArray()));
		} catch (IOException e) {
			// shouldn't happen
			e.printStackTrace();
		}
		return null;
	}
	// make sure we know which children to visit 
	public static int[] gpi(int i, int n) {
		if (i == 0) {
			return new int[]{0, 0};
		} else if (i == n-1) {
			return new int[] {i-1, i-1};
		} else {
			return new int[] {i-1, i};
		}
	}
	// Here's where the real magic happens
	public static int traverse(List<Object> tr, int n, int[] acc) {
		if (tr.isEmpty()) {
			return Arrays.stream(acc).reduce((x, y) -> Math.max(x, y)).getAsInt();
		} else if (n == 1) {
			int[] x = (int[]) tr.remove(0);
			return traverse(tr, n+1, x);
		} else {
			int[] x = (int[]) tr.remove(0);
			for (int i = 0; i < x.length; i++) {
				// dynamic programming (choosing the greater of the two parents)
				x[i] += Math.max(acc[gpi(i, n)[0]], acc[gpi(i, n)[1]]);
			}
			return traverse(tr, n+1, x);
		}
	}
	public static void main(String[] args) {
		String filepath = "../pe067.txt";
		int answer = traverse(read(filepath), 1, new int[]{});
		System.out.printf("Answer: %d", answer);
	}
}
