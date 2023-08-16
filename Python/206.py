from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive
        if head == None or head.next == None:
            return head
        
        res = self.reverseList(head.next)
        
        head.next.next = head

        head.next = None

        return res


        # Iterative Approach

        # if not head:
        #     return None
        # arr = []
        # node = head
        # while node:
        #     arr.append(node)
        #     node = node.next
        
        # for i in range(len(arr) - 1, 0, -1):
        #     arr[i].next = arr[i - 1]

        # arr[0].next = None

        # return arr[-1]
