class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # iterating though the list to find the least no of the sequence
        # check if there's i-1 in the set , if true continue iterating
        # if not add +1 and check if there is in the set until it break
        # at the same time count each time we add +1
        helper = set(nums)
        helper2 = set()
        i, max_leng, num = 0, 0, 0
        while i < len(nums):
            if nums[i] - 1  not in helper or nums[i] not in helper2:
                count = 0           
                num = nums[i]
                while num in helper:
                    helper2.add(num)
                    count += 1
                    num += 1
                max_leng = max(max_leng, count)
            i += 1        
        return max_leng


                        





