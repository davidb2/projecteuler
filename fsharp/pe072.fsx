let rec fact q f i =
    if q % i = 0 then fact (q / i) (f * i) i
    else (q, f)
let size = 2 + 1000000
let phi : int[] = Array.zeroCreate size
phi.[1] <- 1
let mutable min_n, n_o_t = 0, float System.Int32.MaxValue
for i in 2..(size-1) do 
    // if n is prime, totient(n) = n-1
    if phi.[i] = 0 then 
        phi.[i] <- i - 1 
        for j in 2..(size/i)-1 do
            if phi.[j] <> 0 then
                let q, f = fact j (i-1) i
                let n = i*j
                phi.[n] <- f * phi.[q]
printfn "%u" ((Array.sum (Array.map int64 phi)) - ((Array.last>>int64) phi) - 1L)