import Data.Map (fromList, lookup)
import Prelude hiding (lookup)
import Data.Maybe (fromJust)
import Numeric (showHex)
import Data.Char (toUpper)

helper :: (Int, Int, Int) -> Int -> (Int, Int, Int)
helper (_,b,c) 1  = (1,b,c)
helper (a,_,c) 2  = (a,1,c)
helper (a,b,_) 3  = (a,b,1)
helper (a,b,c) _  = (a,b,c)

ans :: Int -> Integer
ans n = sum [ways (helper (0,0,0) d1) (n-1) | d1 <- [2..16]]
        where
            ways (1,1,1) 0  = 1
            ways (_,_,_) 0  = 0
            ways (1,1,1) dl = 16^dl
            ways (a,b,c) dl =
                sum $ map
                    (\nd ->
                        let (x,y,z) = helper (a,b,c) nd in
                            fromJust $ lookup (x, y, z, dl-1) wa)
                    [1..16]
            wa = fromList [
                 ((a', b', c', dl'), ways (helper (a',b',c') nd') dl')
                                                  | dl' <- [0..n]
                                                  , nd' <- [1..16]
                                                  , c' <- [0,1]
                                                  , b' <- [0,1]
                                                  , a' <- [0,1]]
main :: IO ()
main = print $ map toUpper $ (showHex $ sum $ map ans [1..16]) ""