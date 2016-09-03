let ip n = 
    ((string (n) + string (n*2)).ToCharArray() 
        |> Array.map (fun i -> int i - int '0') 
        |> Array.sort) = ([|1..9|]) 
let max = [9111..9999] 
          |> List.filter ip 
          |> List.max
let ans = string (max) + string (max*2)
printfn "%s" ans