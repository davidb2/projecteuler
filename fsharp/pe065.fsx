#r "FSharp.PowerPack.dll"
open Microsoft.FSharp.Math
open System
let e n =
    let f = function
    | x when x%3 = 0 -> 2N*((bignum.FromInt (x/3))+1N)
    | x              -> 1N
    let rec expansion i n = 
        match i with
        | x when x = n -> f x
        | x            -> (f x) + 1N/(expansion (i+1) n)
    in  if n = 0 then 2N
        else 2N + 1N/(expansion -1 (n-2))
(e 99).Numerator.ToString().ToCharArray() 
|> Array.map (fun i -> int i - int '0')
|> Array.sum
|> printfn "%d"