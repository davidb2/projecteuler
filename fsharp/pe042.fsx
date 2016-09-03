open System
let t = Seq.initInfinite (fun n -> (n*(n+1))/2)
 
let isTriangular (w:string) = 
    let s = w.ToCharArray() 
            |> Array.map (fun i -> int i - ((int 'A') - 1)) 
            |> Array.sum
    let quad n = (sqrt (float(8*n+1)) - 1.0) / 2.0
    (quad s) % floor (quad s) = 0.0

// updated from last year
let ans = 
    System.IO.File.ReadAllText("../pe042.txt")
        .Replace("\"", "")
        .Split(',')
    |> Array.filter isTriangular 
    |> Array.length
printf "%d" ans