class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, 11, 12):
        prev = dummy = ListNode(None)

        while l1 and l2:
            if l1.val < l2,val:
                prev.next = 11
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        prev.next = l1 or l2
        return dummy.next