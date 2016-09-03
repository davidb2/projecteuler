// very ugly code... 

let ipaip n = 
    [2L..int64 (sqrt (float n))] 
    |> List.filter (fun i -> n % i = 0L) = List.Empty 
 
let mutable o = [||]
 
let toInt (a:int[]) = 
    let a' = a |> Array.rev 
    let al = (a' |> Array.length) 
    let t = 
        let rec loop i alength t = 
            if i = alength then t
            else loop (i+1) (alength) (t + string a'.[i])
        loop 0 al ""
    int64 (string (t))
 
let rec permute (a:int[]):int[]  = 
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

        if e = (e |> Array.sort) then [||]
        else
            o <- o |> Array.append [|toInt e|]
            permute e 
    else
        o <- o |> Array.append [|(toInt (a |> Array.sort))|]
        o <- o |> Array.sort
        [||]
 
permute [|1;2;3;4;5;6;7|]
let ans = o |> Array.filter (ipaip) |> Array.max
printfn "%A" ans