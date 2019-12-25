# 74. Search a 2D Matrix (Medium)
# https://leetcode.com/problems/search-a-2d-matrix/

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false

# TODO: Approach 1: Binary Search           [O(log(nm)) & O(1)]

from typing import List


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type List[List[int]]
        :type int
        :rtype bool
        """

        if not matrix:
            return False

        return False


if __name__ == "__main__":
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 13

    s = Solution()
    print(s.searchMatrix(matrix, target))
