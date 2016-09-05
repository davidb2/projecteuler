largestPrimeFactor :: Int -> Int
largestPrimeFactor n = lpf n 3 where
                       lpf num d
                         | num == d         = d
                         | num `rem` d == 0 = lpf (num `div` d) d
                         | otherwise        = lpf num (d+2)
main :: IO ()
main = print $ largestPrimeFactor 600851475143