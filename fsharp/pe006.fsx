let sq n = pown n 2
let sqos n = n |> List.sum |> sq
let sosq n = n |> List.map sq |> List.sum
let a = [1..100] |> sqos
let b = [1..100] |> sosq
let ans = a - b
printfn "%d" ans