from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for index, element in enumerate(nums):
            if element in map:
                return [map[element], index]
            map[target - element] = index
