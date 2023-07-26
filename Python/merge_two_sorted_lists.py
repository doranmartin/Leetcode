from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = curr = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 if list1 else list2

        return merged_list.next

'''
create head var for head of merged list
create curr for curr node of merged list
while both lists are not empty:
  compare the current values,
  add the lower value to merged list,
  increment to next node in the one with lower value

after that one list should be empty so:
while list1 or list2 is not empty:
  point to that node with curr node of merged list

'''
