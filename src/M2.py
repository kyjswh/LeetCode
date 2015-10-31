class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start1 = l1
        start2 = l2
        prev1 = l1
        prev2 = l2

        while start1 and start2:
            if start1.val <= start2.val:
                while start1 and start1.val <= start2.val:
                    prev1 = start1
                    start1 = start1.next
                prev1.next = start2
            else:
                while start2 and start2.val < start1.val:
                    prev2 = start2
                    start2 = start2.next
                prev2.next = start1

        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            if l1.val <= l2.val:
                return l1
            else:
                return l2
