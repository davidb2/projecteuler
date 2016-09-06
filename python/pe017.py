nums = [
           [''],
           ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'],
           ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']  ,
           ['', 'one'+'hundred', 'two'+'hundred', 'three'+'hundred', 'four'+'hundred', 'five'+'hundred', 'six'+'hundred', 'seven'+'hundred', 'eight'+'hundred', 'nine'+'hundred'],
           ['', 'one'+'thousand']
      ]
teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
a = 'and'
ans = 0
for i in range(1001):
   digits = str(i)
   n = ''
   for j in reversed(list(range(len(digits)))):
       if j==1 and digits[-2]=="1" and digits[-1]=="0":
           ans += len(nums[j+1][int(str(i)[len(digits)-1-j])])
           n += nums[j+1][int(str(i)[len(digits)-1-j])]
       elif j==1 and digits[-2]=="1" and digits[-1]!="0":
           ans += len(teens[int(digits[-1])])
           n += teens[int(digits[-1])]
           break
       else:
           ans += len(nums[j+1][int(str(i)[len(digits)-1-j])])
           n += nums[j+1][int(str(i)[len(digits)-1-j])]
   if i>100 and i%100!=0:
       ans += len(a)
       n += a
   print(n)
print(ans)