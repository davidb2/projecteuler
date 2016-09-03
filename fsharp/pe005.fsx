// horrible iterative, mutable solution (when i was first learning F#)
let mutable n = 20
let lcm a b = 
    let mutable x = 0
    let mutable y = 0
    if a >= b then
        x <- a
        y <- b
    else
        x <- b
        y <- a
    n <- x
    while x%y <> 0 do
        x <- x + n
    x
let ans = [1..20] |> List.reduce lcm
printfn "%d" ans