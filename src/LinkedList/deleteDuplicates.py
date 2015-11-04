__author__ = 'Daniel'


# Given a sorted linked list, remove all the duplicate items
# For instance,
#       input: 1 -> 1 -> 1 -> 2 -> 2 -> 3
#       output: 1 -> 2 ->3

#Solution:
#   Maintain two pointers p1 and p2
#   if p2's element is equal to p1's element, make p1 pointing to p2's next element and move p2 by 1
#   else make p1 equal to p2, and move p2 by 1


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):

    def deleteDuplicates(self, head):
        if head == None:
            return head

        p1 = head
        p2 = head.next

        dummyHead = ListNode('dummy')
        dummyHead.next = head

        while p1 and p2:
            if p1.val == p2.val:
                p1.next = p2.next
                p2 = p2.next
            else:
                p1 = p2
                p2 = p2.next

        return dummyHead.next