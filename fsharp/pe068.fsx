// adding to the List module
module List = 
    let rec private insertions x = function
        | []             -> [[x]]
        | (y :: ys) as l -> (x::l)::(List.map (fun x -> y::x) (insertions x ys))

    let rec permutations = function
        | []      -> seq [[]]
        | x :: xs -> (permutations xs) |> Seq.collect (insertions x)   
(*
    magic 3-gon ring
    a x y
    b y z
    c z x
*)
(*
    magic 5-gon ring
    a v w
    b w x
    c x y
    d y z
    e z v
*)
let rec ways alpha omega prev_sum acc =
    match alpha, omega with
    | [], _ -> System.String.Join ("", (Seq.rev acc))
    | x::xs, y::y'::ys -> 
        if x+y+y' = prev_sum then 
            ways xs (y'::ys) prev_sum ((string y')::(string y)::(string x)::acc)
        elif prev_sum < 0 && x <= abs(prev_sum)/2+1 && x = List.min (x::xs) then 
            let new_sum = x+y+y'
            ways xs ((y'::ys)@[y]) new_sum ((string y')::(string y)::(string x)::acc)
        else ""
    | _, _ -> failwith "wtf"

[1..10] 
|> List.permutations 
|> Seq.map (List.splitInto 2) 
|> Seq.map (fun s -> ways s.[0] s.[1] -10 [])
|> Seq.filter ((<>)System.String.Empty)
|> Seq.max
|> printfn "%s"