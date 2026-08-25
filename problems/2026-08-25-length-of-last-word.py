# Name: H4D33D
# Problem: Length Of Last Word
# Difficulty: Easy
# Date: 2026-08-25
# Time Taken: 1 Hour

########## PROBLEM ##########

# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 
# Constraints:
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

########## SOLUTION ##########

class Solution(object):
    def lengthOfLastWord(self, s):

        index = len(s) - 1
        # len(s) gives the number of characters; - 1 gives the index of the last character because indexes start at 0.

        while s[index] == " ": # Checking for spaces, move left is so.
            index = index - 1

        count = 0

        while index >= 0 and s[index] != " ": # Making sure we are still within the string and checking for non spaces, move left and count+ if so.
            count += 1
            index = index - 1
        
        return count

# Test Cases:
solution = Solution()
print(solution.lengthOfLastWord("Hello World"))
print(solution.lengthOfLastWord("   fly me   to   the moon  "))
print(solution.lengthOfLastWord("luffy is still joyboy"))

# Inital Idea: 
# Would have to start at the end
# Account for spaces at the end
# Go right to left, checking each character, adding to a counter.
# Once we encounter another space/nothing, we know we are at the beg of last word
# Done. 