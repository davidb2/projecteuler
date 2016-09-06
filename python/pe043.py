# d1 - could be any digit
# d2 - could be any digit
# d3 + d4 + d5 must be divisible by 3
# d4 must be 0 2 4 6 8
# d6 must be 0 or 5
# if d7 > d8 then d7 - d8 = d6; if d7 < d8 then d6 + d8 - d7 = 11;

def permute(nums):
   i = -1
   for a in reversed(range(len(nums)-1)):
       if nums[a] < nums[a+1]:
           i = a
           break
   if i == -1:
       return -1
   j = 0
   for b in reversed(range(len(nums))):
       if nums[b] > nums[i]:
           j = b
           break
   temp = nums[i]
   nums[i] = nums[j]
   nums[j] = temp
   nums[i+1:len(nums)] = list(reversed(nums[i+1:len(nums)]))
   return nums
ans = []
l = [1,0,2,3,4,5,6,7,8,9]
while l != -1:
   if (l[0]!=0 and
       (l[5]==0 or l[5]==5) and 
       (l[3]%2==0) and 
       int(''.join(map(str, l[4:7])))%7==0 and
       int(''.join(map(str, l[6:9])))%13==0 and
       int(''.join(map(str, l[7:10])))%17==0 and
       ((l[2]+l[3]+l[4])%3==0) and 
       ((l[6]>l[7] and l[6]-l[7]==l[5]) or (l[6]<l[7] and l[5]+l[7]-l[6]==11) or (l[6]==l[7] and l[5]==0))):
       ans.append(int(''.join(map(str, l))))
   l = permute(l)
print(sum(ans))