main :: IO ()
main = print $ ((^2) $ sum a) - (sum $ map (^2) a) where a = [1..100]