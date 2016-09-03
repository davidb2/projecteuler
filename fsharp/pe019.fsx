let mutable num = 0
let mutable first = 2
let regularYear = [3;0;3;2;3;2;3;3;2;3;2;3]
let leapYear = [3;1;3;2;3;2;3;3;2;3;2;3]
let countSundaysonFirst year =
    let mutable count = 0
    let isLeapYear y = 
        if y % 4 = 0 then
            leapYear 
        else
            regularYear
    for i in isLeapYear year do
        if first = 7 then num <- num + 1
        first <- first + i
        while first > 7 do first <- first - 7
[1901..2000] |> List.iter (fun year -> countSundaysonFirst year)
printfn "%d" num