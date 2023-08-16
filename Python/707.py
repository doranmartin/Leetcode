class ListNode:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        

    def get(self, index: int) -> int:
        if index < 0 or index > self.size - 1:
            return -1

        if index < self.size / 2:
            node = self.head
            while index > 0:
                node = node.next
                index -= 1
        else:
            node = self.tail
            while index > 0:
                node = node.prev
                index -= 1

        return node.data      
        

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size += 1        

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        added = ListNode(val)

        if index < self.size / 2:
            node = self.head
            while index > 0:
                node = node.next
                index -= 1
            added = ListNode(val)
            node.prev.next = added
            added.prev = node.prev
            added.next = node
            node.prev = added

        else:
            index = self.size - index
            node = self.tail
            while index > 0:
                node = node.prev
                index -= 1
            node.next.prev = added
            added.next = node.next
            node.next = added
            added.prev = node
        
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
