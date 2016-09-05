import Data.Vector.Persistent (Vector, fromList)

primes :: [Integer]
primes = 2 : filter isPrime [3..] where
         isPrime a = isPrimeHelper a primes
         isPrimeHelper a (p:ps)
                | p*p > a        = True
                | a `mod` p == 0 = False
                | otherwise      = isPrimeHelper a ps
main :: IO ()
main = print $ primes !! 10000