__author__ = 'Daniel'


"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
"""


def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """

        ans_list = []
        st = ''


        for c in s:
            if c != ' ':
                st+=c
            else:
                if st != '':
                    ans_list.append(st)
                    st = ''

        if st != '':
            ans_list.append(st)

        ans = ''
        l = len(ans_list)
        for i in range(l):
            if i == 0:
                ans = ans + ans_list[l-1-i]
            else:
                ans = ans + ' ' + ans_list[l-1-i]

        return ans

print(reverseWords('1 '))