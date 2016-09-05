import Data.Function (on)
import Data.Array
import Data.List

cols = listArray (0, 1000000) [c x | x <- [0..]]

c 0  = 0
c 1  = 0
c n' = let next = f n' in
           if next <= 1000000 then 1 + (cols ! next) else 1 + c next

f x  = if even x then x`div`2 else 1+3*x

collatz' :: Int -> Int
collatz' n = cols ! n

main :: IO ()
main = print $ maximumBy (compare `on` collatz') [0..1000000]