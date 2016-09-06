coins = [1,2,5,10,20,50,100,200]
pways = {key: 0 for key in list(range(201))}
pways[0] = 1
for c in coins:
   for s in range(c,201):
       pways[s] += pways[s-c]
print(pways[200])