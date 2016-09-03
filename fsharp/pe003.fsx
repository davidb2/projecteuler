let f n = 
    [2L..int64(sqrt(float n))+1L] 
    |> List.filter(fun i -> n%i=0L)
 
let ip n = 
    0 = (n |> f |> List.length)
 
let lpf n =
    f n 
    |> List.filter ip
    |> List.max
 
let ans = lpf 600851475143L
printf "%d" ans