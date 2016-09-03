let isPrime n = 
    [2..int (sqrt (float n))] 
    |> List.filter (fun i -> n % i = 0) = List.Empty
 
let isSame m n = 
    (m.ToString().ToCharArray() 
    |> Array.map (fun j -> int j - int '0') 
    |> Array.sort) = (n.ToString().ToCharArray()
    |> Array.map (fun j -> int j - int '0') 
    |> Array.sort)
 
let o = [1000..3340] |> List.filter (fun i -> 
                                            (isPrime i) && 
                                            (isPrime (i+3330) && isSame i (i+3330)) && 
                                            (isPrime (i+6660) && isSame i (i+6660)))
 
printfn "%d%d%d" (o.[1]) (o.[1] + 3330) (o.[1] + 6660)