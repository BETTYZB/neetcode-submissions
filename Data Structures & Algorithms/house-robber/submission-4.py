class Solution:
    def rob(self, nums: List[int]) -> int:
        # [1,1,3,3] = [1, 3] =4
        # [2,9,8,3,6] = 9, 3 = 12
        # [2,9,8,3,6]  = [16,9,14,3,6] [2, ]
        # [1, 1, 3, 3] = [4,4,3,3]
        
        r1, r2 = 0, 0
        for n in nums:
            temp = max(n + r2, r1)
            r2 = r1
            r1 = temp

        return r1

        # time - o(n), space-o(1)
        #[12,16]
