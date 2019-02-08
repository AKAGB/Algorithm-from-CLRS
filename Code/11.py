class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res, l = 0, len(height)
        m, n = 0, l - 1
        res = 0
        while m <= n:
            res = max(res, (n - m) * min(height[m], height[n]))
            if height[m] < height[n]:
                m += 1
            else:
                n -= 1
        return res