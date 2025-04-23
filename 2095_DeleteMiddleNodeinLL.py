class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow = head
        fast = head
        prev_slow = None

        while fast and fast.next is not None:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        prev_slow.next = prev_slow.next.next
        return head
