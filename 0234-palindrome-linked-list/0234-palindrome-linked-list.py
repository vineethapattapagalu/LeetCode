# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list_vals=[]
        while head:
            list_vals.append(head.val)
            head = head.next
        if list_vals == list_vals[::-1]:
            return True
        return False
        