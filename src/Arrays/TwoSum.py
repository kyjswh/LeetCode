__author__ = 'Daniel'


class TwoSum:
    '''
    A TwoSum class that supports the following operations:
    a. add(input): Add the number input to an internal data structure
    b. find(value): Find if there exists any pair of numbers whose sum is equal to the input value
    '''
    def __init__(self, l = []):

        self.lst = l

    def add(self, input):
        '''
        Add the input number to a specific position
        :param input:
        :return: None, Modify internal data structure
        '''
        pos = self.__bsearch(input)

        #Add the element to the position and shift each subsequent ones by an offset
        #BSearch takes O(logn) time, and insert takes O(n) time
        start = pos
        inserted = input
        while start < len(self.lst) - 1:
            cur = self.lst[start]
            self.lst[start] = inserted
            inserted = cur
            start += 1

        self.lst.append(inserted)

    def find(self,value):
        '''
        Given an input value find if there exists a pair of numbers whose sum is equal to value
        :param value:
        :return: return the indexes of those two numbers (non zero-based)
        '''
        d = {}

        for i in range(len(self.lst)):
            cur = self.lst[i]
            if value - cur in d.keys():
                return True

            d[cur] = i
        return False

    def __bsearch(self, input):
        '''
        Find the position for the input to be inserted in
        :param input:
        :return: The insert position the input
        '''

        L = 0
        R = len(self.lst) - 1
        M = (L + R)//2
        if R < L:
            return 0
        while L <= R:
            M = (L + R)//2
            #print(M)
            if input <= self.lst[L]:
                return L
            elif input >= self.lst[R]:
                return R + 1
            elif input > self.lst[M]:
                L = M + 1
            else:
                R = M

if __name__ == '__main__':
    t = TwoSum()
    t.add(3)
    t.add(5)
    t.add(8)
    t.add(9)
    t.add(0)
    t.add(-4)
    print(t.lst)
    print(t.find(17))
    print(t.find(-4))
    print(t.find(8))










