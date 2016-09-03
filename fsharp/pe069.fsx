let isPerm (arr1:int[]) (arr2:int[]) = 
    if arr1.Length <> arr2.Length then false
    else
        let mutable zeros = 10
        let hashMap : int[]  = Array.zeroCreate 10
        for d in arr1 do 
            hashMap.[d] <- hashMap.[d] + 1
            if hashMap.[d] = 1 then zeros <- zeros - 1
        for d in arr2 do 
            hashMap.[d] <- hashMap.[d] - 1
            if hashMap.[d] = 0 then zeros <- zeros + 1
        zeros = 10
//////////////////
let rec intToArray n acc = 
    if n < 10 then List.toArray (n::acc)
    else intToArray (n/10) ((n%10)::acc)
// factorization
let rec fact q f i =
    if q % i = 0 then fact (q / i) (f * i) i
    else (q, f)
let size = pown 10 7
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
                let r = (float (n))/(float phi.[n])
                let a, b = 
                    intToArray n [],
                    intToArray phi.[n] [] 
                    in 
                        if isPerm a b && r < n_o_t then
                            min_n <- (n)
                            n_o_t <- r
printfn "%d %f" min_n n_o_t