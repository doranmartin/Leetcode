from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = []
        # for i in range(2):
        #     for num in nums:
        #         ans.append(num)
        
        # return ans

        '''
        clever answer from solutions tab:
        '''

        return nums.extend(nums) or nums
