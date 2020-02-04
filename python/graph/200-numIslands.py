# 200. Number of Islands (Medium)
# https://leetcode.com/problems/number-of-islands/

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# Input:
# 11110
# 11010
# 11000
# 00000
# Output: 1

# Input:
# 11000
# 11000
# 00100
# 00011
# Output: 3

# TODO: Approach 1: DFS for Graph (Accepted)
# Time complexity : O(M×N) where M is the number of rows and N is the number of columns.
# Space complexity : worst case O(M×N) in case that the grid map is filled with lands where DFS goes by M×N deep.
# Intuition: Treat the 2d grid map as an undirected graph and there is an edge between two horizontally or vertically adjacent nodes of value '1'.
# Algorithm: Linear scan the 2d grid map, if a node contains a '1', then it is a root node that triggers a Depth First Search. 
# During DFS, every visited node should be set as '0' to mark as visited node. 
# Count the number of root nodes that trigger DFS, this number would be the number of islands since each DFS starting at some root identifies an island.

# TODO: Approach 2: BFS for Graph (Accepted) 

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        return 0


if __name__ == "__main__":
    matrix = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    s = Solution()
    print(s.numIslands(matrix))