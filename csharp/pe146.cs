using System;


namespace ProjectEuler
{
    class pe146
    {
        static readonly int LIMIT = 150000000;
        static List<Int64> primes;

        static void PrimeSieve()
        {
            bool[] ps = Enumerable.Repeat(true, LIMIT + 1).ToArray();
            ps[0] = false;
            ps[1] = false;
            for (int step = 3; step <= LIMIT / 2; step += 2)
            {
                if (ps[step])
                {
                    for (int p = step * step; p <= LIMIT; p += 2 * step)
                    {
                        ps[p] = false;
                    }
                }
            }
            primes = new List<Int64>();
            primes.add(2);
            for (int i = 3; i <= LIMIT; i += 2)
            {
                if (ps[i])
                {
                    primes.add(i);
                }
            }
        }

        static void Main(string[] args)
        {

        }
    }
}