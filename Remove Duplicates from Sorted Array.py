from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        replace=1
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                nums[replace]=nums[i]
                replace+=1
        return replace  

solution = Solution()

nums = [0,0,1,1,1,2,2,3,3,4]

result = solution.removeDuplicates(nums)

print(nums[:result])