class Solution:
    def middleNode(self, head: OPtional[ListNode]) -> Optional[ListNode]:
        slow, faxt = head, head

        while fast and fast.next:
            slow = slow .next
            fast = fast.next.next
        return slow