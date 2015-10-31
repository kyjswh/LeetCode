__author__ = 'Daniel'


'''
Given two sorted lists, do an in-place merge
'''


#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        l = []
        p = self
        while p != None:
            l.append(p.val)
            p = p.next
        return str(l)


def MergeTwoList(l1,l2):
    start1 = l1
    start2 = l2

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

if __name__ == '__main__':
    n1 = ListNode(1)
    #n1.next = ListNode(3)
    #n1.next.next = ListNode(5)
    print(n1)

    n2 = ListNode(2)
    #n2.next = ListNode(4)
    #n2.next.next = ListNode(6)
    print(n2)

    print(MergeTwoList(n1,n2))