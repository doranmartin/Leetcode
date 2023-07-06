import typing

map = {}
nums = [2, 7, 11, 15]
target = 9

for index, element in enumerate(nums):
    if element in map:
        print([map[element], index])
    map[target - element] = index
