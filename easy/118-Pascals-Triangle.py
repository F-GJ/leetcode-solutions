"""
Question link : https://leetcode.com/problems/pascals-triangle/description/?envType=problem-list-v2&envId=array


Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


Example 2:
Input: numRows = 1
Output: [[1]]
"""


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1]]
        for i in range(1, numRows):
            prev_row = triangle[i - 1]

            current_row = [1]
            for j in range(1, len(prev_row)):
                val = prev_row[j - 1] + prev_row[j]
                current_row.append(val)
            current_row.append(1)
            triangle.append(current_row)
        return triangle


example_one = Solution()
print(example_one.generate(5))


example_two = Solution()
print(example_two.generate(1))
