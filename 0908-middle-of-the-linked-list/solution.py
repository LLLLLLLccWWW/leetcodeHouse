# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head

        # 當 fast 和 fast.next 都存在時，繼續往前走
        while fast and fast.next:
            slow = slow.next    # 慢指標走 1 步
            fast = fast.next.next   # 快指標走 2 步

        return slow
