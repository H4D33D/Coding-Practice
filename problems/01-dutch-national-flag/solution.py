"""
Name:        Hadeed Fawad
Problem:     Dutch National Flag Problem (a.k.a. Sort Colors)
Difficulty:  Medium
Date:        2026-08-24
Time Taken:  TODO - fill in how long this actually took you

Problem statement:
    Given an array containing only 0s, 1s, and 2s, sort it in place so that
    all 0s come first, then all 1s, then all 2s. Do it in one pass using
    O(1) extra space (no counting sort / no built-in sort).

Approach:
    Three-pointer partitioning (Dijkstra's Dutch National Flag algorithm).
    Maintain three pointers:
        low  - boundary, everything before this is a confirmed 0
        mid  - current element being examined
        high - boundary, everything after this is a confirmed 2
    Walk `mid` through the array:
        - if nums[mid] == 0: swap with low, advance both low and mid
        - if nums[mid] == 1: it's already in place, just advance mid
        - if nums[mid] == 2: swap with high, advance high only
          (don't advance mid - the swapped-in value hasn't been checked yet)
    Stop when mid crosses high. Single pass, O(n) time, O(1) space.
"""


def sort_colors(nums: list[int]) -> list[int]:
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


if __name__ == "__main__":
    test_cases = [
        [2, 0, 2, 1, 1, 0],
        [2, 0, 1],
        [0],
        [1],
        [2, 2, 2],
        [],
        [1, 0, 2, 1, 0, 2, 0, 1, 2],
    ]

    for case in test_cases:
        original = case.copy()
        result = sort_colors(case)
        print(f"{original} -> {result}")
        assert result == sorted(original), f"FAILED on {original}"

    print("\nAll test cases passed.")
