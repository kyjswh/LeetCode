__author__ = 'Daniel'

"""
Given a sorted list (ascending order)
Find the index of an element which is equal to a target number
"""

class BinarySearch:
    def solution(self, lst, target):
        Left = 0
        Right = len(lst) - 1

        while Left <= Right:
            i = (Left + Right)/2
            if lst[i] == target:
                return i
            elif lst[i] < target:
                Left = i + 1
            else:
                Right = i - 1

        return -1



