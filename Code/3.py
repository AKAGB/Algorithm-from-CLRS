class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 暴力法
        # result = 0
        # for i in range(len(s)):
        #     k = i + 1
        #     ss = set([s[i]])
        #     while k < len(s) and s[k] not in ss:
        #         ss.add(s[k])
        #         k += 1
        #     result = max(result, k - i)
        # return result

        # 滑动窗口法
        # 可用在找满足某谓词的最长子串
        i, l = 0, len(s)
        d = dict()
        result = 0
        for j in range(l):
            if s[j] in d:
                i = max(i, d[s[j]])
            result = max(result, j - i + 1)
            d[s[j]] = j + 1
        return result

# sol = Solution()
# r = sol.lengthOfLongestSubstring("bziuwnklhqzrxnb")
# print(r)