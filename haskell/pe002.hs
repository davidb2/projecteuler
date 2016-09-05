import Data.List

evenFibSum :: Int
evenFibSum = sum $ filter even fibs
             where
                 fibs = unfoldr (\(a, b) -> if b >= 4000000 then Nothing else Just(b, (b, a+b))) (0, 1)

main :: IO ()
main = print evenFibSum