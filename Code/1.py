class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, a in enumerate(nums):
            try:
                j = nums.index(target - a)
            except:
                continue
            if j != -1 and j != i:
                return [i, j]