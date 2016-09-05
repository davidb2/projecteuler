import Data.Map (fromList, lookup)
import Prelude hiding (lookup)
import Data.Maybe (fromJust)
-- L = 1
-- O = 2
-- A = 3
-- ways (prev_prev_digit, prev_digit) lates days_left
prizes :: Int -> Integer
prizes n = sum
            [ways (d1, d2) ls (n-2)
            | d1 <- [1..3]
            , d2 <- [1..3]
            , d1 + d2 /= 2
            , let ls = if d1 == 1 || d2 == 1 then 1 else 0]
    where
        ways :: (Int, Int) -> Int -> Int -> Integer
        ways (_, _) _ 0   = 1
        ways (a, b) ls dl = sum
                               [fromJust $ lookup (b, c, ls', dl-1) wa
                               | c <- [1..3]
                               , a + b + c /= 9
                               , let ls' = if c == 1 then ls+1 else ls
                               , ls' < 2]
        wa = fromList [((a, b, ls, dl), ways (a, b) ls dl)
                      | a <- [0..3]
                      , b <- [0..3]
                      , ls <- [0..1]
                      , dl <- [0..n-1]]
main :: IO ()
main = print $ prizes 30