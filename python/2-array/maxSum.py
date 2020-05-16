
import sys
from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)

        current_sum, max_sum = -sys.maxsize-1, -sys.maxsize-1
        current_sum1, min_sum = sys.maxsize, sys.maxsize

        for i in range(n):
            current_sum = max(A[i], A[i] + current_sum)
            max_sum = max(max_sum, current_sum)

            current_sum1 = min(A[i], A[i] + current_sum1)
            min_sum = min(min_sum, current_sum1)

        sumA = sum(A)
        sum1 = max_sum
        sum2 = sumA - min_sum if sumA != min_sum else max_sum

        return max(sum1, sum2)


if __name__ == "__main__":
    nums = [1, -2, 3, -2]     # ? Output = 3
    # nums = [5, -3, 5]           # ? Output = 10
    # nums = [-2, -3, -1]         # ? Output = -1

    s = Solution()
    result = s.maxSubarraySumCircular(nums)

    print("Result is {}".format(result))
