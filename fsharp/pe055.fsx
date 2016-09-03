open System
open System.Numerics
let p (n:bigint) = BigInteger.Parse(String.Concat(n.ToString().ToCharArray() |> Array.rev))
let ip n = n = p n          // bool function
let rec isl (n:bigint) (k:int) = 
    if k > 50 then true
    elif ip n && k > 0 then false
    else isl (n + p n) (k+1)
let ans = [10I..10000I] 
          |> List.filter (fun i -> isl i 0) 
          |> List.length
printfn "%d" ans