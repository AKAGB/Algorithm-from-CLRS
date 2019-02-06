class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 1 or l == 0:
            return l

        m, n = l // 2 - 1, l // 2
        if s[m] != s[n]:
            m1 = m2 = m - 1
            n1 = n2 = n + 1
            while m1 >= 0 or n2 < l:
                flag = True
                if m1 >= 0 and s[m1] not in s[m1+1:n+1]:
                    m1 -= 1
                    flag = False
                if n2 < l and s[n2] not in s[m:n2]:
                    n2 += 1
                    flag = False
                if flag:
                    break
            while m2 >= 0 or n1 < l:
                flag = True
                if m2 >= 0 and s[m2] not in s[m2+1:n2]:
                    m2 -= 1
                    flag = False
                if n1 < l and s[n1] not in s[m1+1:n1]:
                    n1 += 1
                    flag = False
                if flag:
                    break
        
            result = max(n1 - m1, n2 - m2) - 1
        else:
            result = 1
        if result <= l // 2:
            ls = self.lengthOfLongestSubstring(s[:l//2])
            rs = self.lengthOfLongestSubstring(s[l//2:])
            result = max(result, ls, rs)

        return result

sol = Solution()
r = sol.lengthOfLongestSubstring("bziuwnklhqzrxnb")
print(r)