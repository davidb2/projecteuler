main :: IO ()
main = print $ sum [x | x <- [0..999], x `rem` 3 == 0 || x `rem` 5 == 0]