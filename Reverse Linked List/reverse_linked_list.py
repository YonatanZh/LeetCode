# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        prev = head
        curr = head.next
        while curr:
            head.next = curr.next
            curr.next = prev
            prev = curr
            curr = head.next
        return prev
