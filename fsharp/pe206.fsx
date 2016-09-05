let isPd (n:int64) = 
   let n2 = pown n 2
   let w = n2.ToString().ToCharArray() 
           |> Array.map (fun i -> int i - int '0')
   let final = Array.create 10 true
   for i in 0..2..18 do 
       if w.[i] <> (i/2+1)%10 then 
           final.[(i/2+1)%10] <- false
   final |> Array.filter id |> Array.length = 10 

let one = [|1010101030L..100L..1389026630L|] |> Array.tryFind (isPd)
let two = [|1010101070L..100L..1389026670L|] |> Array.tryFind (isPd)
[one; two] 
|> List.filter (fun x -> x.IsSome) 
|> List.iter (fun x -> printfn "%u" x.Value)