import Math.Combinatorics.Exact.Binomial
import Data.Function.Memoize

t' :: Integer -> Integer
t' 1 = 0
t' n = (n-1) + 2 * t'(n-1)

t :: Integer -> Integer
t = memoize t'

a :: Integer
a = 26

main :: IO ()
main = print $ maximum $ map (\x -> (a `choose` x) * t x) [1..a]