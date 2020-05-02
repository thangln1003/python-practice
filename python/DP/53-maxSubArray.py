""" 53. Maximum Subarray (Easy)
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. """

# * Input: [-2,1,-3,4,-1,2,1,-5,4],
# * Output: 6
# * Explanation: [4,-1,2,1] has the largest sum = 6.

# ? Follow up:
# ? If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# TODO: Approach 1: Devide and Conquer                              [O(NlogN) & O(logN)]
# TODO: Approach 2: Greedy                                          [O(N) & O(1)]
# TODO: Approach 3: Dynamic Programming (Kadane's algorithm)        [O(N) & O(1)]

from typing import List
import numpy as np


class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        result = 0

        return result

    def maxSubArray2(self, nums: List[int]) -> int:
        result = 0

        return result

    def maxSubArray3(self, nums: List[int]) -> int:
        result = 0

        return result


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    s = Solution()
    # result = s.maxSubArray1(nums)
    result = s.maxSubArray2(nums)
    # result = s.maxSubArray3(nums)

    print("Result is {}".format(result))
