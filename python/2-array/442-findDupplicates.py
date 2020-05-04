""" 442. Find All Duplicates in an Array (Medium)
https://leetcode.com/problems/find-all-duplicates-in-an-array/

Given an array of integers, 
!Constraint: 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

*Input: [4, 3, 2, 7, 8, 2, 3, 1]
*Output: [2, 3] """

# TODO: Based on Constraint, we use negative number to check visited index in array 

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        N = len(nums)

        for i in range(N):
            index = abs(nums[i]) - 1    # ? Cover case when nums[i] = N

            if nums[index] < 0:         # ? Jump in this index twice
                result.append(abs(nums[i]))
            else:
                nums[index] = -nums[index]

        return result


if __name__ == "__main__":
    # nums = [4, 3, 2, 7, 8, 2, 3, 1]  # ? Output = [2, 3]
    nums = [1, 1, 3, 5, 2, 8, 5, 3]  # ? Output = [1, 5, 3]

    s = Solution()
    result = s.findDuplicates(nums)

    print("Result is {}".format(result))
