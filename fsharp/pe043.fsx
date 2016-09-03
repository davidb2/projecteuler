let toInt (a:int[]) =
    let len = a |> Array.length 
    let rec loop (b:int[]) (s:string) l ol = 
        if l = 0 then s
        else loop b (s+string(b.[ol-l])) (l-1) ol
    int64(loop a "" len len)
let property n = 
    let n' = n.ToString().ToCharArray() |> Array.map (fun i -> int i - int '0') 
    n' |> Array.length = 10 &&
    toInt (Array.sub n' 1 3) % 2L = 0L &&
    toInt (Array.sub n' 2 3) % 3L = 0L &&
    toInt (Array.sub n' 3 3) % 5L = 0L &&
    toInt (Array.sub n' 4 3) % 7L = 0L &&
    toInt (Array.sub n' 5 3) % 11L = 0L &&
    toInt (Array.sub n' 6 3) % 13L = 0L &&
    toInt (Array.sub n' 7 3) % 17L = 0L
 
let rec permute a s = 
    let k = 
        let l = (a |> Array.length) - 2 
        let rec loop k' = 
            if k' = -1 then -1
            elif a.[k'] < a.[k' + 1] then k'
            else loop (k' - 1)
        loop l
    if k <> -1 then
        let b = (a |> Array.filter (fun l -> a.[k] < l))
        let l = a |> Array.findIndex (fun i -> i = b.[(b |> Array.length) - 1])
        //swap 
        a.[k] <- a.[k] + a.[l]
        a.[l] <- a.[k] - a.[l]
        a.[k] <- a.[k] - a.[l] 
        
        let d = Array.sub a (k+1) ((a |> Array.length) - 1 - k) |> Array.rev |> Array.toList
        let c = Array.sub a 0 (k+1) |> Array.toList
        let e = c@d |> List.toArray

        if e = (e |> Array.sort) then s
        else
            if property (toInt e) then permute e (s+(toInt e))
            else permute e s
    else s
 
let sum = permute [|0..9|] 0L
printfn "%A" sum