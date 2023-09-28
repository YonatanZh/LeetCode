# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        runner = head.next
        val_list = []
        while runner is not None:
            val_list.append(runner.val)
            runner = runner.next

        curr = head.next
        end = len(val_list) - 1
        start = 0
        flag = True
        while curr is not None:
            if flag:
                curr.val = val_list[end]
                end -= 1
                flag = False
            else:
                curr.val = val_list[start]
                start += 1
                flag = True
            curr = curr.next
