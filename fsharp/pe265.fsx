module List = 
    let cycle n arr = 
        let ll = List.length arr
        let m = n % ll
        let t = m + if m < 0 then ll else 0
        let f, s = arr |> List.splitAt t
        s @ f
    let flatten arr = 
        arr |> List.reduce (@)

let tryFindValidCycle n start = 
    let rec fillBins i n acc =
        match i with
        | s when s = n -> acc
        | _            -> acc |> Map.add i 0 |> fillBins (i+1) n

    let rec tryFindValidCycle' i n availableCycles acc set (totalAcc:int list list) currentCycle =
        if i = (1 <<< n) then [acc |> List.rev]
        else 
            let hash = currentCycle >>> 1
            let bin = availableCycles |> Map.find hash
            if bin > 2 || set |> Set.contains currentCycle then [[]]
            else 
                let updatedMap = availableCycles |> Map.add hash (bin ||| (1 <<< (currentCycle &&& 1)))
                let updatedSet = set |> Set.add currentCycle
                let frontBits  = (currentCycle &&& ((1 <<< (n-1))-1))
                let nextAcc    = currentCycle :: acc
                let firstAttempt = (frontBits <<< 1) |> tryFindValidCycle' (i+1) n updatedMap nextAcc updatedSet totalAcc
                let secondAttempt = ((frontBits <<< 1) ||| 1) |> tryFindValidCycle' (i+1) n updatedMap nextAcc updatedSet totalAcc
                firstAttempt @ secondAttempt @ totalAcc
    let bins = Map.empty |> fillBins 0 (1 <<< (n-1)) |> Map.add (start &&& ((1 <<< (n-1))-1)) ((start &&& 1) + 1)
    start |> tryFindValidCycle' 0 n bins [] Set.empty [[]]

let rec computeValue i n acc list = 
    match i, list with
    | _, []     -> acc
    | i, x::xs -> xs |> computeValue (i+1) n (acc + ((x >>> (n - 1)) <<< i))

let findAllValidCycles n =
    [0..(1 <<< n)-1] 
    |> List.map (fun s -> s |> tryFindValidCycle n |> List.filter (List.isEmpty >> not) |> List.distinct)
    |> List.filter (fun a -> a |> List.length > 0)
    |> List.flatten
    |> List.map (fun a -> a |> List.cycle (a |> List.findIndex ((=)0)))
    |> List.distinct
    |> List.map (fun a -> a |> List.map bigint |> List.rev |> computeValue 0 n 0I)
    |> List.sum

printfn "%A" (findAllValidCycles 5)