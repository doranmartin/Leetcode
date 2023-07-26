from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[k] = nums[i + 1]
                k += 1

        return k
        
'''
keep track of current index
keep track of next available "free" space
iterate over array checking if the next element is the same as current
k will be the number of unique elements

'''
