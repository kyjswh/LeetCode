__author__ = 'Daniel'


#Given a list, move all zero elements to the end of list while maintaining the relative order of the remaining elements
#Do it in-place

#Solution:
# Keep two pointers, p1 and p2, while p1 is always behind p2
# Swap p1 and p2 if arr[p1] = 0  and arr[p2] != 0, increment two pointers
# if arr[p1] and arr[p2] both equal to zero, you want increment p2 until it is not zero, then do the swap:
# In the remaining situations we should all increment two pointers by 1 because they have the correct order

class solution(object):

    def moveZeroes(self,nums):

        i = 0
        j = 1

        while i < len(nums) and j < len(nums):
            if nums[i] == 0 and nums[j] == 0:
                j += 1
            else:
                if nums[i] == 0 and nums[j] != 0:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                i+=1
                j+=1