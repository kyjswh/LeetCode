__author__ = 'Daniel'


"""
Dynamic Programming solves the problem of reaching an optimal
state via a series of sub-optimal states
"""


"""
input: an integer array, and a target number
output: the minimum number of integer elements that sum to the target number
"""
def DP1(nums, target):
    min_states = [float("inf") for i in range(target+1)]

    min_states[0] = 0
    for i in range(1, target+1):
        for j in nums:
            if j <= i and min_states[i-j] + 1 < min_states[i]:
                min_states[i] = min_states[i-j] + 1

    return min_states[target]

def DP2(nums, target):

    min_states = [float("inf") for i in range(target+1)]

    min_states[0] = 0
    for val in nums:
        for i in range(1, target+1):
            if val <= i and min_states[i-val] + 1 < min_states[i]:
                min_states[i] = min_states[i-val]+1

    return min_states[target]


"""
Given a sequence of numbers A = [a1,a2,a3,....]
Find the longest non-decreasing sub-sequence

State: sub optimal state i represents the length of longest non decreasing sequence that ends with A[i]

"""
def findLogestNonDecreasing(nums):
    states = [1 for i in range(len(nums))]

    for j in range(1, len(nums)):
        if nums[j-1] <= nums[j]:
            states[j] = states[j-1] + 1

    max = (float('-inf'),float('-inf'))


    for s in enumerate(states):
        if s[1] > max[1]:
            max = s

    return nums[(max[0]+1-max[1]):(max[0]+1)]


print(findLogestNonDecreasing([5,3,4,8,6,7]))

"""
Length of longest substring without repeating characters
"""

def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        states = [1 for i in range(len(s))]

        if len(states) == 0:
            return ''


        for i in range(1,len(states)):
            flag = True
            starting = i-states[i-1]

            for j in range(i-states[i-1], i):
                if s[j] == s[i]:
                    starting = j + 1

            states[i] = i - starting + 1

        max = (float('-inf'), float('-inf'))

        for t in enumerate(states):
            if t[1] > max[1]:
                max = t

        return max[1]


print(lengthOfLongestSubstring('dvdf'))






arr = [1,3]
print(DP1(arr,3), DP2(arr,3))