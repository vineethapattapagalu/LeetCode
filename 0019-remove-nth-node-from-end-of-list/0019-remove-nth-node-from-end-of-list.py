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
        
        if head == None:
            return head
        len_list = 0
        temp_head = head
        while temp_head:
            len_list += 1
            temp_head = temp_head.next
        temp_head = ListNode(None)  
        temp_head.next = head
        result = temp_head
        nth_from_start = len_list - n
        while nth_from_start >= 0:
            if nth_from_start == 0:
                temp_head.next = temp_head.next.next
            else:
                temp_head = temp_head.next
            nth_from_start -= 1
        return result.next
        