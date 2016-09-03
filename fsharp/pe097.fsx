let (%%) a n = bigint.Remainder(a, n)
let (^^) a n = bigint.Pow(a, n)
printfn "%A" (((28433I*(2I ^^ 7830457))+1I)%%10000000000I)