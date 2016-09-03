let powers =
    [|0..9|]
    |> Array.map (fun i -> pown i 5)
let ans =
    [|10..413343|]
    |> Array.filter (fun t ->
        t.ToString().ToCharArray()
        |> Array.map (fun u -> int u - int '0')
        |> Array.sumBy (fun v -> powers.[v]) = t)
    |> Array.sum
printfn "%d" ans