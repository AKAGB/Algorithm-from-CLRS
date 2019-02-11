class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        table = [['']]
        for i in range(1, n+1):
            table.append([])
            for j in range(i):
                table[i].extend(['(' + x + ')' + y for x in table[j] for y in table[i-1-j]])
        return table[n]

sol = Solution()
print(sol.generateParenthesis(3))