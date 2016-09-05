import Data.Vector ((!), fromList)
import System.Environment (getArgs)

ans :: Int -> Integer
ans 0 = 0
ans 1 = 9
ans 2 = 45
ans n = sum [ways d1 d2 (n-2) | d1 <- [1..9], d2 <- [0..9]]
        where
            ways _ _ 0    = 1
            ways pd cd dl = sum $ map (\nd -> wa ! cd ! nd ! (dl-1)) [0..(9-pd-cd)]
            wa = fromList [fromList [fromList [
                 ways pd' cd' dl' | dl' <- [0..n]]
                                  | cd' <- [0..9]]
                                  | pd' <- [0..9]]
main :: IO ()
main = do
    args <- getArgs
    let n = read $ head args :: Int
    print $ ans n