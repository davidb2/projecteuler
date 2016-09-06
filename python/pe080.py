from decimal import *
from math import sqrt, floor
getcontext().prec = 102
def digital_sum(n): 
    if floor(sqrt(n))**2 != n:
        return sum(map(int, str(Decimal.sqrt(Decimal(n))).replace('.', '')[:100]))
    else:
         return 0
print(sum(map(digital_sum, range(100))))