# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        pA = headA
        pB = headB

        # 當 pA 和 pB 不相等時就繼續走
        while pA != pB:
            # pA 往前走，如果走到盡頭就換到 headB；否則繼續 next
            pA = pA.next if pA else headB
            # pB 往前走，如果走到盡頭就換到 headA；否則繼續 next
            pB = pB.next if pB else headA

        # 這裡回傳 pA 或 pB 都可以
        # 如果相交，它們會停在相交節點；如果不相交，它們會同時停在 None

        return pA
        
