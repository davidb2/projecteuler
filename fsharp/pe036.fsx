open System
let toBinary (n:int) = System.Convert.ToString(n, 2)
let isPalindromic (n:string) = 
    let ns = n.ToCharArray() |> Array.map (fun i -> int i - int '0')
    let rec loop a = 
        if a |> Array.length = 1 then true
        elif a |> Array.length = 2 then a.[0] = a.[1]
        elif a.[0] = a.[a.Length-1] then loop a.[1..a.Length-2]
        else false
    loop ns 
let ans = [1..2..999999] 
        |> List.filter (fun i -> isPalindromic (string i) && isPalindromic (toBinary i))
        |> List.sum
printfn "%d" ans