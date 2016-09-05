module Main where
import Data.Vector (fromList, (!))

ways :: Int -> Int -> Int
ways m n = calc m n where
           calc 0 _ = 1
           calc _ 0 = 1
           calc x y = (c ! (x-1) ! y) + (c ! x ! (y-1))
           c = fromList [fromList [calc x y | y <- [0..n]] | x <- [0..m]]

main :: IO ()
main = print $ ways 20 20