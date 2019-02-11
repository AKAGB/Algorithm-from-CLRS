class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for each in s:
            if each == '[' or each == '(' \
                or each == '{':
                stack.append(each)
            elif len(stack) > 0 and \
                    abs(ord(stack[-1]) - ord(each)) <= 2:
                stack.pop(-1)
            else:
                return False
        return len(stack) == 0