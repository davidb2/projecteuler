num = int(600851475143)
temp = num
for factor in range(2, num+1):
    while temp%factor==0:
        temp = int(temp/factor)
    if temp==1:
        print(factor)
        break