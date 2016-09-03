let d n = 
    [1..n/2] 
    |> List.filter (fun i -> n % i = 0) 
    |> List.sum
let isAmicable n = 
    let b = d n
    let a = d b
    a = n && a <> b
let ans = [2..9999] 
        |> List.filter isAmicable 
        |> List.sum
printfn "%d" ans