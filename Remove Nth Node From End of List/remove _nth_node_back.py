# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        reverse_head, size = self.reverseList(head)
        if size == 1:
            return None
        elif n == size:
            return self.reverseList(reverse_head)[0].next
        if n == 1:
            return self.reverseList(reverse_head.next)[0]
         
        curr = reverse_head
        for i in range (1, size + 1):
            if i + 1 == n:
                curr.next = curr.next.next
                break
            curr = curr.next
        
        return self.reverseList(reverse_head)[0]

        
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        prev = head
        curr = head.next
        size = 1
        while curr:
            head.next = curr.next
            curr.next = prev
            prev = curr
            curr = head.next
            size += 1
        return prev, size
