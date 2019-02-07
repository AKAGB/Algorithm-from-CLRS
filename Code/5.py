class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s = s
        l = len(s)
        if l == 1 or l == 0:
            return s
        ans = [0, 0]
        for i in range(0, l - 1):
            n, m = i - 1, i + 1
            n, m = self.myCheck(n, m)
            if ans[1] - ans[0] < m - n:
                ans = [n, m]

            n, m = i, i + 1
            n, m = self.myCheck(n, m)
            if ans[1] - ans[0] < m - n:
                ans = [n, m]

        return s[ans[0]+1: ans[1]]

    def myCheck(self, n, m):
        l = len(self.s)
        while n >= 0 and m < l and self.s[m] == self.s[n]:
            n -= 1
            m += 1
        return n, m

sol = Solution()
res = sol.longestPalindrome('aas')
print(res)