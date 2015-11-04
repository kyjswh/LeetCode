__author__ = 'Daniel'


def convert(s, numRows):

    if numRows == 1:
        return s

    str_arr = ['' for i in range(numRows)]

    for i in range(len(s)):
        if (i/(numRows-1))%2 == 0:
            str_arr[i%(numRows-1)] += s[i]
        else:
            str_arr[numRows-1-i%(numRows-1)]+=s[i]

    ret_str = ''

    for sub_str in str_arr:
        ret_str += sub_str
    return ret_str


print(convert("PAYPALISHIRING",2))




