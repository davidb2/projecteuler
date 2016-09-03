open System.IO
open System.Text.RegularExpressions
let totriangle s = 
    (Regex.Replace(s, "\\s+", " ")).Trim().Split([|' '|])
    |> Array.map (string>>int)
let read filepath = 
    File.ReadAllLines(filepath)
    |> Array.map totriangle
    |> Array.toList
let gpi i n = 
    if i = 0 then 0,0
    elif i = n-1 then i-1,i-1
    else i-1,i
let rec traverse n a tr = 
    match tr, n with
    | [], _ -> Array.max a
    | x::xs, 1 -> traverse (n+1) (x) (xs)
    | x::xs, y -> 
        traverse (n+1) (Array.mapi (fun i e -> 
            e + max a.[fst (gpi i y)] a.[snd (gpi i y)]) x) (xs)
let ans = 
    "../pe018.txt"
    |> read 
    |> traverse 1 [||]
printfn "%i" ans 