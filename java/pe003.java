public class pe003
{
    public static long lpf (long num)
    {
        long tempnum = num;
        long ans = 0;
 
        for (long factor = 2; factor < num/2; factor++) 
        {
            while (tempnum % factor == 0) 
            {
                tempnum /= factor;
            }
            if (tempnum == 1) 
            {
                ans = factor;
                break;
            }
        }
        return ans;
    }
 
    public static void main (String[] args)
    {
        System.out.println (lpf(600851475143L));
    }
}