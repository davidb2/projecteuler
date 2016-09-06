def p(n):
   perms = []
   i = 1
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
   while n != -1 and i != 1000000:
       n = permute(n)
       i += 1
   return int(''.join(list(map(str, n))))
ans = p([0,1,2,3,4,5,6,7,8,9])
print(ans)