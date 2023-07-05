from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if bool(nums) is False:
            return []
        
        list = [nums[0]]

        for index in range(1, len(nums)):
            list.append(list[index - 1] + nums[index])

        return list
