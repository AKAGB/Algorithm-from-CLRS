class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        if len(nums) <= 1:
            return len(nums)
        while i < len(nums):
            while i < len(nums) and nums[i] == nums[i-1]:
                nums.pop(i)
            i += 1
        return len(nums)