#nowarn "40"

open System.Collections.Generic

/// quick modular exponentiation; equivalent to ModPow
let rec qe = 
    let cache = Dictionary<uint64, uint64>()
    fun a n k -> 
        match n with
        | 0UL -> 1UL
        | 1UL -> a
        | _  -> 
            if cache.ContainsKey(n) then cache.[n]
            else
                let half = n / 2UL
                let p = n % 2UL
                cache.[n] <- (((qe a half k) % k) * ((qe a (half + p) k) % k) % k)
                cache.[n]

/// modular hyperexponentiation
let rec he a n k = 
    match n with
    | x when x = 1UL -> a
    | _              -> qe a (he a (n-1UL) k) k

let a = 1777UL
let k = 1885UL
let m = 100000000UL
printfn "%u" (he a k m)