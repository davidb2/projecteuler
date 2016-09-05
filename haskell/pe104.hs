import Data.Vector (Vector, fromList, (!))
import Data.List (findIndex, unfoldr)
import Data.Maybe

fibs :: [Integer]
fibs = unfoldr (\(x,y) -> Just(y, (y, x+y))) (0,1)

fun' :: Vector Int
fun' = fromList [2,3,5,7,11,13,17,19,23]

fun :: Int -> Int
fun n = fun' ! n

ip :: Integer -> Int -> Bool
ip 0 acc = acc == 223092870
ip n acc = r /= 0 && acc `rem` f /= 0 && ip d (acc*f)
             where
                 (d, r) = n `quotRem` 10
                 f = fun (fromIntegral r-1)
main :: IO ()
main = do
    let a = fromJust
               $ findIndex
                 (\x -> let num = x `rem` (10^9) in
                    ip num 1 && ip ((read $ take 9 $ show x) :: Integer) 1) fibs
    print $ a+1