# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:  # 兩個都還有節點才比較
            if list1.val <= list2.val:
                curr.next = list1  # 接上 list1 的節點
                list1 = list1.next  # list1 往前走
            else:
                curr.next = list2   # 接上 list2 的節點
                list2 = list2.next  # list2 往前走
            curr = curr.next    # curr 往前走

        # 其中一個走完了，把另一個剩下的直接接上
        curr.next = list1 if list1 else list2

        return dummy.next

        
