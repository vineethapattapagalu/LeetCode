# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#         result = head
#         while True:
#             dic = {}
#             index = []
#             temp_head = head
#             i = 0
#             while temp_head:
#                 dic[i] = temp_head.val
#                 temp_head = temp_head.next
#                 i += 1
#             i = 0 
#             print(dic)
#             for i in range(len(dic)):
#                 temp_sum = 0
#                 j = i
#                 while j< len(dic):
#                     temp_sum += dic[j]
#                     if temp_sum == 0:
#                         index.append([i, j])
#                         break
#                     j += 1
#                 if index != []:
#                     break
#             if index == []:
#                 break
#             result = ListNode(None)
#             result.next = head
#             temp_head = result
#             i, j = 0, 0
#             while temp_head:
#                 if i >= index[0] and i <= index[1]:
#                     temp_head.next = temp_head.next.next
#                 else:
#                     temp_head = temp_head.next
#                 i += 1
#             head = result.next
#             print(head)
#         return result.next

        dummy = ListNode(0)
        dummy.next = head
        prefix_sum_map = {}
        prefix_sum = 0
        node = dummy
        while node:
            prefix_sum += node.val
            prefix_sum_map[prefix_sum] = node
            node = node.next
        
        prefix_sum = 0
        node = dummy
        while node:
            prefix_sum += node.val
            if prefix_sum in prefix_sum_map:
                node.next = prefix_sum_map[prefix_sum].next
            node = node.next

        return dummy.next

