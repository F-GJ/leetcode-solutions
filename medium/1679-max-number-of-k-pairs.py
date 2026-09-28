class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        indexed_nums = sorted((val, idx) for idx,val in enumerate(nums))
        left = 0
        right = len(nums) - 1
        pairs_found = []
        indices_to_remove = set()

        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            if current_sum == k:
                pairs_found.append(
                    (indexed_nums[left][0], indexed_nums[right][0])
                )
                indices_to_remove.add(indexed_nums[left][1])
                indices_to_remove.add(indexed_nums[right][1])
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1
        nums[:] = [val for idx, val in enumerate(nums) if idx not in indices_to_remove]
        return len(pairs_found)

