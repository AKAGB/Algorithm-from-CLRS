class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        l = len(nums)
        res = []
        i = 0
        while i < l:
            target = -nums[i]
            left = i + 1
            right = l - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([-target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
            while i < l and target == -nums[i]:
                i += 1
        return res

sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))