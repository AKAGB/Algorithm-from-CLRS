class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if x[0] == '-':
            res = int('-' + x[:0:-1])
            if res < -(2**31):
                res = 0
        else:
            res = int(x[::-1])
            if res > 2**31 - 1:
                res = 0
        return res

# sol = Solution()
# print(sol.reverse('-123'))