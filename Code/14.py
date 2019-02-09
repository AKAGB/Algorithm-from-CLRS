class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        l = min([len(s) for s in strs])
        al = len(strs)
        k = 0
        while k < l:
            flag = True
            for i in range(1, al):
                if strs[i][k] != strs[i-1][k]:
                    flag = False
                    break
            if flag:
                k += 1
            else:
                break
        if k == 0:
            return ""
        return strs[0][:k]