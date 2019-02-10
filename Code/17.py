class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        res = list(mapping[digits[0]])
        for each in digits[1:]:
            tmp = []
            for s in mapping[each]:
                tmp.extend([x + s for x in res])
            res = tmp
        return res

sol = Solution()
print(sol.letterCombinations('23'))