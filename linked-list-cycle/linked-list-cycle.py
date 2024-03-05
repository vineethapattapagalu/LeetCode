# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        set_nodes = set()
        
        while head:
            if head in set_nodes:
                return True
            set_nodes.add(head)
            head = head.next
        return False
            
        