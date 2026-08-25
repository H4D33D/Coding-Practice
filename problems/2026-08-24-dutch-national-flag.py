# Name:        H4D33D
# Problem:     Dutch National Flag Problem (a.k.a. Sort Colors)
# Difficulty:  Medium
# Date:        2026-08-24
# Time Taken:  

########## PROBLEM ##########

# You are given an array nums with n objects colored red, white, or blue, sort them
# in-place so that objects of the same color are adjacent, with the colors in the
# order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue,
# respectively.

# You must solve this problem without using the library's sort function.

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Explanation:
# The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s
# first, then all 1s, then all 2s.

# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

# Explanation:
# The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.

# Constraints:
# - n == nums.length
# - 1 <= n <= 300
# - nums[i] is either 0, 1, or 2.

# Follow up:
# Could you come up with a one-pass algorithm using only constant extra space?

########## SOLUTION ##########

class ColorSorter(object):
    def sortColors(self, nums):
        count0 = 0
        count1 = 0
        count2 = 0

        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        index = 0

        for i in range(count0):
            nums[index] = 0
            index += 1

        for i in range(count1):
            nums[index] = 1
            index += 1

        for i in range(count2):
            nums[index] = 2
            index += 1