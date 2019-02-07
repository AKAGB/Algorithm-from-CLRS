class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s = s.strip()
        minus = ''
        if len(s) == 0:
            return 0
        if s[0] == '-':
            minus = s[0]
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        elif not s[0].isdigit():
            return 0
        res = ''
        for each in s:
            if not each.isdigit():
                break
            res += each
        if len(res) == 0:
            return 0
        res = int(minus + res)
        if -(2**31) > res:
            return -(2**31)
        elif res > 2**31 - 1:
            return 2**31 - 1
        return res

sol = Solution()
print(sol.myAtoi("-91283472332"))