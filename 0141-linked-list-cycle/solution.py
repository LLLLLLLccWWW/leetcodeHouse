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
        # 如果鏈表為空，或者只有一個節點且沒有環，直接回傳 False
        if not head or not head.next:
            return False

        slow = head
        fast = head

        # 因為 fast 每次走兩步，所以要確保 fast 和 fast.next 都存在
        while fast and fast.next:
            slow = slow.next        # 烏龜走一步
            fast = fast.next.next   # 兔子走兩步

            # 如果快慢指針相遇，代表一定有環
            if slow == fast:
                return True

        # 如果兔子走到了終點（None），代表鏈表有盡頭，也就是沒有環
        return False


