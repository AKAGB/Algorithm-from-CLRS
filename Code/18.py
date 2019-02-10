class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def increase(nums, var, direct, cond):
            var += direct
            while (cond - var) * direct > 0 and nums[var] == nums[var - direct]:
                var += direct
            return var

        nums = sorted(nums)
        i, l = 0, len(nums)
        res = []
        while i < l:
            j = i + 1
            while j < l:
                head, tail = j + 1, l - 1
                while head < tail:
                    tmp = nums[i] + nums[j] + nums[head] + nums[tail]
                    
                    if tmp == target:
                        res.append([nums[i], nums[j], nums[head], nums[tail]])
                        tail = increase(nums, tail, -1, head)
                        head = increase(nums, head, 1, tail)
                    elif tmp > target:
                        tail = increase(nums, tail, -1, head)
                    else:
                        head = increase(nums, head, 1, tail)
                j = increase(nums, j, 1, l)
            i = increase(nums, i, 1, l)
        return res

sol = Solution()
print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))