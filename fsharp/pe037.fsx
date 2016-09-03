open System.Collections
open System
 
let isPrime n =
    if n > 5 && (n % 2 = 0 || n % 3 = 0 || n % 5 = 0) then
        false
    elif n < 2 then
        false
    else
        [(2.)..(Math.Sqrt(double(n)))] |> Seq.exists (fun x -> n % int x = 0) |> not
 
let isTruncatable (n:int) = 
    let q = new ArrayList()
    let p = n.ToString().ToCharArray() |> Array.map (fun i -> int i - int '0')
    for j in 1..(p |> Array.length) do
        ignore (q.Add( int (String.Concat((Array.sub p 0 j))) |> isPrime ) )
    for i in 1..(p |> Array.length) - 1 do
        ignore (q.Add( int ( String.Concat( Array.sub p i ( (p |> Array.length) - i) ) ) |> isPrime))
    let r = Array.create q.Count true
    ignore (q.CopyTo(r))
    (r |> Array.filter ((=)true) |> Array.length) = (2 * ((p |> Array.length) - 1) + 1)
 
let ans = 
    [|11..999999|] 
    |> Array.filter isPrime 
    |> Array.filter isTruncatable 
    |> Array.sum
printfn "%d" ans