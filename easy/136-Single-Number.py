"""
Question link : https://leetcode.com/problems/single-number/?envType=problem-list-v2&envId=array

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        total = 0

        for num in nums:
            total ^= num
        return total


print("=" * 10, " Example 1 ", "=" * 10)
example_1 = Solution()
nums_1 = [2, 2, 1]
print(f"Input: nums = {nums_1}")
print(f"Output: {example_1.singleNumber(nums_1)}")

print("=" * 10, " Example 2 ", "=" * 10)
example_2 = Solution()
nums_2 = [4, 1, 2, 1, 2]
print(f"Input: nums = {nums_2}")
print(f"Output: {example_2.singleNumber(nums_2)}")


print("=" * 10, " Example 3 ", "=" * 10)
example_3 = Solution()
nums_3 = [1]
print(f"Input: nums = {nums_3}")
print(f"Output: {example_3.singleNumber(nums_3)}")
