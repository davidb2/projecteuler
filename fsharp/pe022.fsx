open System
let nameScore (name:string) index = 
    // if index = 0, position = 1st...
    (name.ToCharArray() 
    |> Array.map (fun i -> bigint (int i - int 'A' + 1)) |> Array.sum) * 
    bigint (index + 1)
 
let names = String.Concat((System.IO.File.ReadLines("../pe022.txt") 
            |> Seq.item 0).ToCharArray() 
            |> Array.filter(fun i -> i <> '"')).Split ',' 
            |> Array.sort 
            |> Array.mapi (fun i name -> nameScore name i) 
            |> Array.sum
printfn "%A" names