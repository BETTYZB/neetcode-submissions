class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones[0]
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        
        while len(stones) >= 2:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, x-y)
        

        return -stones[0] if stones else 0