let isPalindrome n =
    (n.ToString().ToCharArray() 
    |> Array.rev 
    |> Array.map(fun i -> i.ToString()) 
    |> Array.fold(fun acc a -> acc+a) "") = n.ToString()
let mutable palindromes = [||]
for i in 100..999 do
    for j in 100..999 do
        let product = i*j
        if product |> isPalindrome then
            palindromes <- palindromes |> Array.append [|product|]
let ans = palindromes |> Array.max
printfn "%d" ans