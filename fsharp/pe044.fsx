open System
let p = Seq.initInfinite (fun n -> (int64 n)*(3L*(int64 n)-1L)/2L)
 
let quad (a:int64) (b:int64) (c:int64) = 
    let discriminant = Math.Sqrt(double (b * b) - double (4L * a * c))
    int ((double (-b) + discriminant)/double (2L*a))
 
let inP n = 
    n = (p |> Seq.item (quad 3L -1L -(n + n)))
 
let rec property a b = 
    let j = if b = 1 then a else b-1
    let k = if j = a then a+1 else a
    let pj = p |> Seq.item j  
    let pk = p |> Seq.item k
    if inP(pj + pk) && inP (abs (pk - pj)) then
        printfn "Pj:%d\tPk:%d\tD:%d" pj pk (abs(pk-pj))
        (abs(pk-pj))
    else property k j
 
let ans = property 2 1
printfn "%d" ans