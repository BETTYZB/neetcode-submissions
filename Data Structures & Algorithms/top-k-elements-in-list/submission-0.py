class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_frq = Counter(nums)

        buck = [[] for _ in range(len(nums) + 1)]
        res = []

        for i in dict_frq:
            buck[dict_frq[i]].append(i)

        for i in range(len(buck) - 1, -1, -1):
            for j in range(len(buck[i])):
                if k > 0:
                    res.append(buck[i][j])
                    k -= 1

        return res

