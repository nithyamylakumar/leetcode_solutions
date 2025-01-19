
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        for num in nums:
            if i < 2 or num != nums[i-2]:
                nums[i] = num
                i +=1

        return i
    

myobject = Solution()

nums = [1,1,1,2,2,3,3]
newarray = myobject.removeDuplicates(nums)

print("length of new array", newarray)
print("array", nums[:newarray])
