class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Define
        MIN = -2147483648
        def singleDiv(ded, div):
            res = 0
            while ded >= div:
                res += 1
                ded -= div
            return res, ded

        if dividend == MIN and divisor == -1:
            # overflow
            return 2147483647
        minus = False
        if (dividend < 0 and divisor > 0) or \
            (dividend > 0 and divisor < 0):
            minus = True
        dividend = str(abs(dividend))
        divisor = str(abs(divisor))

        i = 0
        remain = ''
        res = '0'
        while i < len(dividend):
            j = i + 1
            while j < len(dividend) and int(remain + dividend[i:j]) < int(divisor):
                j += 1
                res += '0'
            tmp, remain = singleDiv(int(remain + dividend[i:j]), int(divisor))
            res += str(tmp)
            remain = str(remain)

            i = j
        if minus:
            res = '-' + res

        return int(res)

sol = Solution()
print(sol.divide(0, 1))