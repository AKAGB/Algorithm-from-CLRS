class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def equal(st, md):
            return md == '.' or md == st 
        k = 0
        i = 0
        while i < len(p):
            if i < len(p) - 1 and p[i+1] == '*':
                obj = p[i]
                j = k
                while j < len(s) and equal(s[j], obj):
                    if self.isMatch(s[j+1:], p[i+2:]):
                        return True
                    j += 1
                i += 1
            elif k >= len(s):
                return False
            elif equal(s[k], p[i]):
                k += 1
            else:
                return False
            i += 1
        if k < len(s):
            return False
        return True

sol = Solution()
print(sol.isMatch('a', 'ab*'))