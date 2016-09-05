load 'regex'
a                     =: fread '../pe011.txt'
matrix                =: 20 20 $ ". ('\n'; ' ') rxrplc (a -. u:13)
max_horizontal        =: >./>./4*/\ matrix
max_vertical          =: >./>./4*/\|: matrix
max_positive_diagonal =: >./>./4*/\"1 , /. matrix
max_negative_diagonal =: >./>./4*/\"1 , /. (|."1) matrix
max_product           =: >./ max_horizontal, max_vertical, max_positive_diagonal, max_negative_diagonal
max_product