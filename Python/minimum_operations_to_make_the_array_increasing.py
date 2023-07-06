from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for i in range(1, len(nums)):
            curr = nums[i]
            if nums[i-1] >= curr:
                nums[i] = nums[i-1] + 1
                operations += nums[i] - curr

        return operations
