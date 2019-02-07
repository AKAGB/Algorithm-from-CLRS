class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # m < n
        m, n = len(nums1), len(nums2)
        imin, imax = 0, m
        while imin <= imax:
            i = (imin + imax) // 2
            j = (m + n + 1) // 2 - i
            if i < imax and nums2[j - 1] > nums1[i]:
                imin = i + 1
            elif i > imin and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    leftMax = nums2[j - 1]
                elif j == 0:
                    leftMax = nums1[i - 1]
                else:
                    leftMax = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return leftMax
                
                if i == m:
                    rightMin = nums2[j]
                elif j == n:
                    rightMin = nums1[i]
                else:
                    rightMin = min(nums1[i], nums2[j])
                return (leftMax + rightMin) / 2
        return 0