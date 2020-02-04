# 4. Median of Two Sorted Arrays (Hard)
# https://leetcode.com/problems/median-of-two-sorted-arrays/

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0

# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5

# TODO: Approach 1: Using sorted()          [O(NlogN) & O(1)]
# TODO: Approach 2: Recursive Approach      [O(log(min(m,n))) & O[1]]

from typing import List


class Solution:
    def findMedianSortedArray1(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        len12 = len(nums)

        if len12 % 2:
            return (nums[len12//2])
        else:
            return (nums[len12//2] + nums[len12//2 - 1]) / 2


    def findMedianSortedArray2(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)

        if len1 > len2:
            return self.findMedianSortedArray2(nums2, nums1)

        low, high = 0, len1
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (len1 + len2 + 1) // 2 - partition1

            maxLeft1 = nums1[partition1 - 1] if partition1 != 0 else float("-inf")
            minRight1 = nums1[partition1] if partition1 != len1 else float("inf")
            maxLeft2 = nums2[partition2 - 1] if partition2 != 0 else float("-inf")
            minRight2 = nums2[partition2] if partition2 != len2 else float("inf")

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (len1 + len2) % 2:
                    return max(maxLeft1, maxLeft2)
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            elif maxLeft1 > minRight2:
                high = partition1 - 1
            else:
                low = partition1 + 1


if __name__ == "__main__":
    # nums1 = [1, 3]
    # nums2 = [2]

    # nums1 = [1, 2]
    # nums2 = [3, 4]

    nums1 = [1, 2, 3]
    nums2 = [4, 5]

    s = Solution()
    # print(s.findMedianSortedArray1(nums1, nums2))
    print(s.findMedianSortedArray2(nums1, nums2))
