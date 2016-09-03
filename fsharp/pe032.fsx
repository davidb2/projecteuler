let rec panDigitalProduct a b ns =
    let ab = a * b
    let c = (string(ab) + string(a) + string(b)).ToCharArray() |> Array.sort
    let d = "123456789".ToCharArray()
    let f = if b = 100 then 1 else b+1
    let e = if f = 1 then a+1 else a
    if c = d then
        printfn "%A * %A = %A" a b ab
        if e = 10000 then (ns |> List.distinct |> List.sum)
        else panDigitalProduct e f (ab::ns)
    else
        if e = 10000 then (ns |> List.distinct |> List.sum)
        else panDigitalProduct e f ns
printfn "%A" (panDigitalProduct 100 1 [])