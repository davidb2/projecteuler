open System
open System.IO
open System.Text.RegularExpressions
open System.Collections.Generic

let FILE = "../pe098.txt"

let printAndPass arr = 
    printfn "%A" arr
    arr

let f = 
    let cache = Dictionary<bigint, bigint>()
    fun n ->
        if not (cache.ContainsKey(n)) then cache.[n] <- 2I * n * n + 29I
        cache.[n]
let key1 str = 
    str |> Seq.map (fun c -> f (bigint (int c - int 'A'))) |> Seq.reduce (*) 
let (<=>) str rgx = Regex.Split(str, rgx)

let (-.) str c = str |> String.filter ((<>)c)

let words = 
    File.ReadAllText(FILE) <=> ","
    |> Array.map (fun str -> str -. '"')
    |> Array.groupBy key1
    |> Array.filter (fun (k, v) -> Array.length v > 1)
    |> Array.map snd

let maxWordLength = 
    words 
    |> Array.maxBy (fun words -> String.length words.[0]) 
    |> Array.item 0 
    |> String.length

let g = 
    let cache = Dictionary<bigint, bigint>()
    fun n ->
        if not (cache.ContainsKey(n)) then cache.[n] <- 2I * n * n + 11I
        cache.[n]
let key2 num = 
    num.ToString().ToCharArray() |> Array.map (fun c -> g (bigint (int c - int '0'))) |> Seq.reduce (*) 

let squares = 
    Seq.unfold (fun x ->
        let x2 = pown x 2
        if int (log10 (float x2)) > maxWordLength then None
        else Some(x2, x+1I)
    ) 0I
    |> Seq.groupBy key2
    |> Seq.map snd
    |> Seq.filter (fun nums -> Seq.length nums > 1)
    |> Seq.groupBy (fun s -> (s |> Seq.item 0) |> (float>>log10>>ceil>>int))
    |> Map.ofSeq

let oneToOne x y = 
    match x, y with
    | a, b when String.length a <> String.length b -> false
    | a, b -> 
        let b0 = 
            (a, b) 
            ||> Seq.zip  
            |> Seq.groupBy fst 
            |> Seq.map (snd>>Seq.distinct)
            |> Seq.tryFind (fun s -> Seq.length s > 1)
            |> Option.isNone
        let b1 = 
            (a, b) 
                ||> Seq.zip  
                |> Seq.groupBy snd 
                |> Seq.map (snd>>Seq.distinct)
                |> Seq.tryFind (fun s -> Seq.length s > 1)
                |> Option.isNone
        b0 && b1

let rec comb n l = 
    match n, l with
    | 0, _ -> [[]]
    | _, [] -> []
    | k, (x::xs) -> List.map ((@) [x]) (comb (k-1) xs) @ comb k xs

let matching (x0, y0) (x1, y1) = 
    oneToOne x0 y0 && 
    oneToOne x1 y1 && 
    (((x0, y0) ||> Seq.zip |> Seq.sort |> Set.ofSeq) = ((x1, y1) ||> Seq.zip |> Seq.sort |> Set.ofSeq))

// i actually got lucky as I missed the triplet anagrams: [post, spot, stop] 
let findMaxMatching lis (mappings: Map<int, seq<seq<bigint>>>) =
    let x0 = lis |> List.head
    let x1 = lis |> List.tail |> List.head

    let temp = 
        mappings 
        |> Map.tryFind (x0 |> String.length)
    if temp.IsNone then 0I
    else 
        let lis0 = 
            temp
            |> Option.get
            |> Seq.toList
            |> List.collect (Seq.toList>>comb 2)
            |> List.filter (fun [y0; y1] -> ((x0, string y0), (x1, string y1)) ||> matching)
        if lis0.IsEmpty then 0I
        else lis0 |> List.maxBy (fun [y0; y1] -> max y0 y1) |> List.max

let ans = 
    words 
    |> Array.map (fun arr -> squares |> findMaxMatching (arr |> Array.toList))
    |> Array.max

printfn "%A" ans