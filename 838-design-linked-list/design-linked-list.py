class ListNode:
    def __init__(self, x):
        self.val = x
        self.next, self.prev = None, None

class MyLinkedList:
    def __init__(self):
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next #initialising the actual head instead of self.head (dummy)
        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.tail and index == 0:
            return cur.val
        return -1
         
    def addAtHead(self, val: int) -> None:
        left, head, newHead = self.head, self.head.next, ListNode(val)
        head.prev = newHead
        newHead.next = head
        left.next = newHead
        newHead.prev = left
        
    def addAtTail(self, val: int) -> None:
        right, tail, newTail = self.tail, self.tail.prev, ListNode(val)
        right.prev = newTail
        newTail.next = right
        tail.next = newTail
        newTail.prev = tail 

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head.next 
        while cur and index > 0:
            cur = cur.next 
            index -= 1

        if cur and index == 0:
            node, left = ListNode(val), cur.prev 
            left.next = node
            node.prev = left
            node.next = cur
            cur.prev = node 

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next 
        while cur and index > 0:
            cur = cur.next 
            index -= 1

        if cur and index == 0 and cur != self.tail:
           prv, nxt = cur.prev, cur.next 
           prv.next = nxt 
           nxt.prev = prv 

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)