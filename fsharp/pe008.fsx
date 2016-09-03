open System.IO
open System
open System.Numerics
let productOf13 n s = 
    Array.sub (n.ToString().ToCharArray()) s 13 
    |> Array.map (fun i -> bigint (int i - int '0')) 
    |> Array.fold (*) 1I
let num = 
    File.ReadAllText("../pe008.txt")
    |> Seq.filter ((<>)('\n'))
    |> Seq.toArray
    |> String 
    |> bigint.Parse
let o = [0..987] |> List.map (fun i -> productOf13 num i)
let max = o |> List.max
let maxi = o |> List.findIndex (fun i -> i = max)
let ans = productOf13 num maxi 
printfn "%A" ans