class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        def generate(num, base):
            if 0 <= num < 4:
                return base[0] * num
            if num == 4:
                return base[0] + base[1]
            if 5 <= num < 9:
                return base[1] + base[0] * (num - 5)
            if num == 9:
                return base[0] + base[2]
        bases = [['I', 'V', 'X'], ['X', 'L', 'C'], ['C', 'D', 'M'],
                    ['M', '', '']]
        res, k = '', 0
        while num:
            x = num % 10
            num //= 10
            res = generate(x, bases[k]) + res
            k += 1
        return res

# sol = Solution()
# print(sol.intToRoman(1994))