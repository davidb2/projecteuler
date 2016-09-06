// takes a minute or two
let LIMIT = pown 10 9
let primes = 
    [2;3;5;7;11;13;17;19;23;29;31;37;41;43;47;53;59;61;67;71;73;79;83;89;97]
let rec factor n p = 
    //printfn "n: %d\tp: %A" n p
    match n, p with
    | 1, _ -> 1
    | n, [] -> 0
    | n, p::ps when n%p=0 -> factor (n/p) (p::ps)
    | n, p::ps -> factor n ps
let rec ans n acc = 
    match n with
    | n when n > LIMIT -> acc 
    | n -> ans (n+1) (acc + (factor n primes))

let a = ans 1 0
printf "%d" a