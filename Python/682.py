from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        sum = 0
        for char in operations:
            if char == '+':
                records.append(records[-1] + records[-2])
            elif char == 'D':
                records.append(2 * records[-1])
            elif char == 'C':
                sum -= records.pop()
                continue
            else:
                records.append(int(char))
            
            sum += records[-1]

        return sum

        '''
        keep track of a stack (will be called 'records')
        keep track of current score

        iterate over operations, and make separate case for each
        '''
