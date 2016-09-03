let psieve limit =
    let bprimes = Array.create (limit+1) true
    bprimes.[0] <- false
    bprimes.[1] <- false
    for i in 2..limit/2 do
        for j in 2*i..i..limit do
            bprimes.[j] <- false
    [0..limit] |> List.filter (fun i -> bprimes.[i]) 
 
let psieve1 limit =
    let bprimes = Array.create (limit+1) true
    bprimes.[0] <- false
    bprimes.[1] <- false
    for i in 2..limit/2 do
        for j in 2*i..i..limit do
            bprimes.[j] <- false
    bprimes
 
let parray = psieve1 2001000
let isPrime n = if n > 0 then parray.[n] else false
 
//number of consecutive primes
let rec nop a b n = 
    if isPrime ((pown n 2) + (a*n) + (b)) then nop a b (n+1)
    else n
 
let mutable max = 0
let mutable pair = (0, 0)
let mutable ans = 0
let bs = psieve 999
 
for a in -999..999 do
    for b in bs do
        let n = (nop a b 0)
        //printfn "a:%d\tb:%d\tn:%d" a b n
        if n > max then
            max <- n
            pair <- (a, b)
            ans <- a * b
printfn "%d" ans