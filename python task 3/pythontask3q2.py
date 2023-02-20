class sum(object):
   def maxSubArray(self, nums):
      s = [0 for i in range(len(nums))]
      s[0] = nums[0]
      for i in range(1,len(nums)):
         s[i] = max(s[i-1]+nums[i],nums[i])
      
      return max(s)
a=int(input("Number of elements in the array:-"))
n=list(map(int, input("elements of array:-").strip().split()))
print(n)
max_sum = sum()
print(max_sum.maxSubArray(n))

