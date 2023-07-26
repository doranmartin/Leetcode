from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[k] != val:
                k += 1
            elif nums[k] == val and nums[i] != val:
                nums[k] = nums[i]
                nums[i] = val
                k += 1
        
        return k


'''
keep track of current 'overwriting' index
iterate over list
if ith == val -> continue
if kth != val -> k++
else kth == val and ith != val -> swap their values
'''

