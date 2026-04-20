class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        for i in nums:
            if i - 1 in num_set:
                continue
            length = 1
            while i + 1 in num_set:
                length += 1
                i += 1

            if length > max_length:
                max_length = length


        return max_length

        