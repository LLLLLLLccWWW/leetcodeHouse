class Solution(object):
    def isPalindrome(self, head):
        # 步驟1：快慢指標找中點
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 步驟2：反轉後半段
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # 步驟3：比較前半段和反轉後的後半段
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
