from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = int((start + end) / 2)
        while start < end:
            val = nums[mid]
            if target == val:
                return mid
            elif target < val:
                end = mid
            else:
                start = mid + 1
            mid = int((start + end) / 2)
        
        if target > nums[mid]:
            return mid + 1
            
        return mid

        '''
        keep track of start, end, midpoint
        while start and endpoint aren't equal:
            go to midpoint
            if target equals mid val:
                then return midpoint
            else if target val less than mid val:
                then set end to midpoint val
            else (target is greater):
                set start to midpoint val
            midpoint = start + end / 2
                
        return midpoint
        '''
