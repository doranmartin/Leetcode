from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        node_list = []
        node_list.append(node)

        while node.next != None:
            node = node.next
            node_list.append(node)
        
        mid = int(len(node_list) / 2)

        return node_list[mid]
