from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        merged = ListNode()



'''
Compare first nodes
whichever is smaller, add that to 

if the other list isn't empty:
append all remaining elements in order

'''
