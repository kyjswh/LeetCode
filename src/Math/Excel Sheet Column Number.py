__author__ = 'Daniel'



#Given a excel column sheet column title 'AA', 'BB', 'C'...
#Return the number of that column
#For instance
#       'A' - 1
#       'B' - 2
#       'C' - 3
#       'D' - 4
#       'E' - 5
#       ....
#       'AA' - 26
#       'AB' - 27
#       'AC' - 28
#       'AD' - 29
#       ....

#Solution: 假设做算数题， 26进制， 从最后一个字符开始， 每进一个字符，乘数因子就要乘以26 然后用乘数因子乘以那一位与‘A'前面那个字符的差值，加到結果裡面

class Solution(object):

    def titleToNumber(self, s):
        i = len(s) - 1
        multip = 1
        res = 0
        while i >= 0:
            res = res + (ord(s[i]) - ord('A') + 1) * multip
            multip = multip * 10
            i -= 1

        return res