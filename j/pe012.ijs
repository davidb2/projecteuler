t    =: -:@:(*: + 1&*)
nod  =: 4 : '#(x-.(~.x)-.y)'
nord =: 3 : '*/>:((q:y) (nod " 1 0) (~.q:y))'
{.(500<((nord " 0)(b=.t>:i.20000x)))#(b)