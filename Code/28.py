class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def getNext(p):
            _next = [0] * (len(p) + 1)
            _next[0] = -1

            i, j = 0, -1
            while i < len(p):
                if j == -1 or p[i] == p[j]:
                    i += 1
                    j += 1
                    _next[i] = j
                else:
                    j = _next[j]
            return _next

        _next = getNext(needle)
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = _next[j]
        if j == len(needle):
            return i - j
        return -1

sol = Solution()
print(sol.strStr('hello', 'll'))