// sorta looks like Haskell code
open System.Collections.Generic
let (+=) (a:bigint ref) (b:bigint) = a := !a + b
let cache                          = Dictionary<int*int*int, bigint>()
let rec count ds                   = 
   match ds with
   | (_,_,0)                            -> 1I
   | (_,_,_) when cache.ContainsKey(ds) -> cache.[ds]
   | (d, d', n)                         -> 
                                           let res = ref 0I
                                           [0..9] 
                                           |> List.iter (fun d'' -> 
                                               if d + d' + d'' <= 9 then
                                                   res += count (d', d'', n-1))
                                           cache.Add((d, d', n), !res)
                                           !res
let ans n =
   if n = 2 then 45I
   elif n = 1 then 9I
   elif n < 1 then failwith "Argument must be grater than 0"
   else 
       let res = ref 0I
       [1..9] |> List.iter (fun d -> 
           [0..9] |> List.iter (fun d' -> 
               res += count (d, d', n-2)))
       !res
printfn "%A" (ans 20)