class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        from math import inf
        nums = sorted(nums)
        l = len(nums)
        i = 0
        res = inf
        while i < l:
            head = i + 1
            tail = l - 1
            while head < tail:
                tmp = nums[i] + nums[head] + nums[tail]
                if tmp == target:
                    return target
                elif tmp > target:
                    tail -= 1
                    while head < tail and nums[tail] == nums[tail + 1]:
                        tail -= 1
                else:
                    head += 1
                    while head < tail and nums[head] == nums[head - 1]:
                        head += 1
                if abs(res-target) > abs(tmp-target):
                    res = tmp
            i += 1
            while i < l and nums[i] == nums[i-1]:
                i += 1
        return res

sol = Solution()
print(sol.threeSumClosest([-1, 2, 1, -4], 1))