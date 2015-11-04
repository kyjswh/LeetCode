__author__ = 'Daniel'


#Given an integer input, sum its the squares of digits together until it reaches 1, if a number is like this it is called 'Happy Number'
# For instance,
#       13 -> 1^2 + 3^2 = 10
#       10 -> 1^2 + 0^2 = 1
#   Thus 13 is a happy number


#Solution: doing experiment helps to find that:
#       if the number is not a happy number, the adding process will loop at some point.
# So we could store the intermediate results into a hash table, then return false once new result exists in the hash table


class Solution(object):
    def HappyNumber(self, num):

        res = num
        d = {}
        d[num] = 1


        while res != 1:
            temp = 0

            while res > 0:
                temp = (res%10)**2
                res = res//10

            if temp in d.keys():
                return False

            else:
                d[temp] = 1
            res = temp

        return True
