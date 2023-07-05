from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for index in range(1, n + 1):
            if index % 15 == 0:
                value = 'FizzBuzz'
            elif index % 3 == 0:
                value = 'Fizz'
            elif index % 5 == 0:
                value = 'Buzz'
            else:
                value = str(index)
            
            answer.append(value)

        return answer
