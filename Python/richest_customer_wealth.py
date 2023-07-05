from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        max, curr = (0, 0)

        for m, list in enumerate(accounts):
            if curr > max:
                max = curr
            curr = 0
            for n, value in enumerate(accounts[m]):
                curr += value

        return max
