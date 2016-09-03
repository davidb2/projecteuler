open System
open System.IO
open System.Text

let _num = 80
let totriangle (s:int[][]) =
    let tri_matrix =
        seq {
            for i = 0 to _num-2 do
                yield [|for j = i downto 0 do yield s.[j].[i-j]|]
            yield [|for j = _num-1 downto 0 do yield s.[j].[_num-1-j]|]
            for i = 1 to _num-1 do
                yield [|for j = _num-1 downto i do yield s.[j].[_num-j+(i-1)]|]
        }
    tri_matrix
    |> Seq.toList
let read filepath =
    File.ReadAllLines(filepath)
    |> Array.map (fun s -> Array.map Int32.Parse (s.Split(',')))
    |> totriangle
let rec traverse a tr =
    match tr with
    | [] -> Array.min a
    | x::xs when Array.isEmpty a -> traverse (x) (xs)
    | x::xs ->
        traverse (Array.mapi (fun i e ->
            if a.Length < x.Length then [i-1; i] else [i; i+1]
            |> List.filter (fun z -> 0 <= z && z < a.Length)
            |> List.map (fun z -> a.[z])
            |> List.min
            |> (+) e) x) (xs)
let ans =
    "matrix.txt"
    |> read
    |> traverse [||]
printfn "%i" ans