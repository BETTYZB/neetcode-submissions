class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)
        val = 1

        for i in range(len(nums) - 1):
            prod[i + 1] = prod[i] * nums[i]

        for i in range(len(nums) - 1, 0, -1):
            prod[i - 1] = prod[i - 1] * val * nums[i]
            val *= nums[i]


        return prod

        