class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = []
        for i in range(numRows):
            res.append([])
        k = 0
        direct = 1
        for each in s:
            if k == numRows:
                k = numRows - 2
                direct = -1
            elif k == -1:
                k = 1
                direct = 1
            res[k].append(each)
            k += direct
        r = ''
        for each in res:
            r += ''.join(each)
        return r

# sol = Solution()
# print(sol.convert("LEETCODEISHIRING", 4))