public class pe72 {
    final static int size = 1000000+1;
    final static int[] phi = new int[size];

    public static void main(String[] args) {
        long sum = 0;

        phi[1] = 1;
        for (int i = 2; i < size; i++) {
            // if n is prime, totient(n) = n - 1
            // we know that "i" must be a prime number
            if (phi[i] == 0) {
                phi[i] = i - 1;
                for (int j = 2; i * j < size; j++) {
                    // if j is prime, we'll get to that when i = j
                    if (phi[j] != 0) {
                        int q = j;
                        int f = i - 1;
                        while (q % i == 0) {
                            f *= i;
                            q /= i;
                        }
                        phi[i * j] = f * phi[q];
                    }
                }
            }
            sum += phi[i];
        }
        System.out.println(sum);
    }
}