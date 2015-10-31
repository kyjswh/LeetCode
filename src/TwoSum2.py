__author__ = 'Daniel'
'''
Another implementation of TwoSum class
Requires O(n) space O(1) add and O(n) find time
The best if number of elements is huge
'''

class TwoSum2:

    def __init__(self):
        self.d = {}


    def add(self, input):
        if input in self.d.keys():
            self.d[input] += 1
        else:
            self.d[input] = 1


    def find(self, target):
        keyList = self.d.keys()

        for n in keyList:
            diff = target - n

            if diff != n and diff in keyList:
                return True
            elif diff == n and self.d[n] > 1:
                return True

        return False

