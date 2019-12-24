# 3. Longest Substring Without Repeating Characters (Medium)
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string, find the length of the longest substring without repeating characters.

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# TODO: Approach 1: Brute Force [O(n*3) & O(1)]
# TODO: Approach 2: Sliding Window (HashMap)
# TODO: Approach 3: Sliding Window Optimized (HashMap)


class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        if len(s) < 1:
            return 0

        if len(s) == 1:
            return 1

        maxLen = 1

        for i in range(len(s)-1):
            for j in range(len(s[i+1::1])):
                # sub = s[i] + s[i+1:i+j+2:1] # Bad performance
                isValid = self.allUnique(s, i, i + j + 1)
                if isValid and j - i +1 > maxLen:
                    maxLen = max(j - i + 1, maxLen)

        return maxLen

    def lengthOfLongestSubstring2(self, s: str) -> int:
        maxLen = 1
        


        return maxLen

    def lengthOfLongestSubstring3(self, s: str) -> int:
        maxLen = 1

        return maxLen

    def allUnique(self, s: str, start: int, end: int) -> bool:
        Dict = {}
        while start < end:
            char = s[start]
            if char in Dict:
                return False
            Dict[char] = start
            start += 1

        return True


if __name__ == "__main__":
    # input = "abcabcbb"
    # input = "abc"
    # input = "ac"
    # input = "cc"
    input = "bbbbb"

    s = Solution()
    print(s.lengthOfLongestSubstring1(input))
    # print(s.lengthOfLongestSubstring2(input))
    # print(s.lengthOfLongestSubstring3(input))
