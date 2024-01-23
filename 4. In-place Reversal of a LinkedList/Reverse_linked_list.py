#Using Two pointer T O(n), S O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while   curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

#Using recusive solution T O(n), S O(n)
class Solution:
    def reverseList(self, head:  ListNode) -> ListNode:
        
        #base
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead