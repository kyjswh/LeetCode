__author__ = 'Daniel'


#Input: 2 sorted array arr1 and arr2, while arr1 has enough length to hold all of the elements in arr1 and arr2
#Output: None
#Effect: merge two sorted arrays in-place, without any extra space


#Solution:
#   we start from the end of both arrays, if one element A is greater than  element B in the other array, then
#   there will be x+y elements before A in the merged array, where x is the number of elements before A in the same array,
#       and y is the number of elements up until B in the other array.
#       we assign the new position to A, and decrement pointer in A's array by 1
#   when finished, it could be the case that the new array is still incomplete! Because there will be remaining elements in the
#   shorter array (think about the extreme case, when every element in long array is greater than every element in short array)
#
#   A final step is to move all the remaining elements from the short array to long array, if there exists any

class Solution(object):
    #Suppose arr1 length > arr2
    def mergeTwoSortedArray(self, arr1, arr2):
        m = len(arr1)
        n = len(arr2)

        i = m - 1
        j = n - 1

        while i >= 0 and j >= 0:
            if arr1[i] > arr[j]:
                arr1[i+j+1] = arr1[i]
                i -= 1
            else:
                arr1[i+j+1] = arr2[j]
                j -= 1

        #Check if shorter array has remaining elements
        while j >= 0:
            arr1[j] = arr2[j]
            j-=1