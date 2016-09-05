load 'regex'
10 {.":+/". (('\n'; 'x ') rxrplc ((fread '../pe013.txt') -. u:13))