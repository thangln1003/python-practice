""" 53. Maximum Subarray (Easy)
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. """

# * Input: [-2,1,-3,4,-1,2,1,-5,4],
# * Output: 6
# * Explanation: [4,-1,2,1] has the largest sum = 6.

# ? Follow up:
# ? If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

from typing import List
import numpy as np


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = 0

        return result


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    s = Solution()
    print("Result is {}".format(s.maxSubArray(nums)))    


