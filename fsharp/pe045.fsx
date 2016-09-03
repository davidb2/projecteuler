open System
let t = Seq.initInfinite (fun n -> (int64 n)*((int64 n)+1L)/2L)
let p = Seq.initInfinite (fun n -> (int64 n)*(3L*(int64 n)-1L)/2L)
let h = Seq.initInfinite (fun n -> (int64 n)*(2L*(int64 n)-1L))
 
let quad (a:int64) (b:int64) (c:int64) =
    let discriminant = Math.Sqrt(double (b * b) - double (4L * a * c))
    int ((double (-b) + discriminant)/double (2L*a))
 
let inT n =
    n = (t |> Seq.item (quad 1L 1L -(n + n)))
 
let inP n =
    n = (p |> Seq.item (quad 3L -1L -(n + n)))
 
let inH n =
    n = (h |> Seq.item (quad 2L -1L -n))
 
let rec loop i k =
    let n = h |> Seq.item i
    if k = 3 then i-1
    elif inT n && inP n then loop (i+1) (k+1)
    else loop (i+1) k
 
let ans = h |> Seq.item (loop 1 0)

printf "%u" ans