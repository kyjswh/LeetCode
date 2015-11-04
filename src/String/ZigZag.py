__author__ = 'Daniel'


def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        i = 0
        ret_arr = []
        while i < len(s):
            r = ['' for m in range(numRows)]
            for j in range(numRows):
                r[j] = s[i]
                i+=1
                if i >= len(s):
                    break

            ret_arr.append(r)

            if i >= len(s):
                break

            for k in range(1, numRows-1):
                t = ['' for m in range(numRows)]
                t[numRows-1-k] = s[i]
                ret_arr.append(t)
                i+=1
                if i >= len(s):
                    break

        ret_str = ''

        for u in range(numRows):
            for v in range(len(ret_arr)):
                ret_str = ret_str + ret_arr[v][u]

        return ret_str

print(convert("PAYPALISHIRING",3))