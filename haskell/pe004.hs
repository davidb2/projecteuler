main :: IO ()
main = print $ maximum [ab |
                            a <- [100..999],
                            b <- [a..999],
                            let ab = a*b,
                            let c = ab in show c == reverse (show c)]