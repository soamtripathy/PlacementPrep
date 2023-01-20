# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        prev = None             # initially prev should points to None
        while temp!=None:
            if temp.val == val and prev == None :      # when first node is val which has to remove
                temp = temp.next
                head = temp
                prev = None                         # prev must None because still first Node equal to val
            elif temp.val == val:               # when in middle node equal to val
                prev.next = temp.next               # simple prev point to next node
                temp = temp.next
            else:                               # Move untill node not equal to val
                prev = temp
                temp = temp.next
        return head