// i wrote this in 2015, not good code
let isAbundant n = 
    ([1..n/2] 
    |> List.filter (fun i -> n % i = 0) 
    |> List.sum) > n
let alist = [0..28123] |> List.filter isAbundant
let n = alist |> List.length
let mutable (table:int list) = List.Empty
for i in alist do
    for j in alist do
        table <- (i+j)::table
table <- table |> List.distinct |> List.sort
let a = table |> List.findIndex (fun i -> i > 28123)
table <- Array.sub (table |> List.toArray) 0 a |> Array.toList
let ans = ((28124*28123)/2) - (table |> List.sum)
printfn "%d" ans 