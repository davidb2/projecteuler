let fib = (0, 1) |> Seq.unfold(fun (a, b) -> Some(a+b, (b, a+b))) 
let nf = fib |> Seq.takeWhile(fun i -> i < 4000000) |> Seq.filter(fun i -> i%2=0)
let ans = nf |> Seq.sum
printfn "%d" ans