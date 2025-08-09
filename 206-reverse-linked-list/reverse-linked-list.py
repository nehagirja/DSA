# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       prev, curr = None, head
    #    time complxity O(n) space O(1)
       while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
       return prev

# **iterative solution**
# store the next of the current in "nxt" variable so that it's location does not get lost when we point the current's next to the previous to make it a tail because prev is actually Null 
# previous is our head because at the last step curr becomes Null, while, in the beginning prev is set to Null 