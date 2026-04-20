class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x , y in points:
            d = math.sqrt((x)**2 + (y)**2)
            minHeap.append([d, [x, y]])

        heapq.heapify(minHeap)
        
        res = []
        while k > 0:
            d, val = heapq.heappop(minHeap)
            res.append(val)
            k -= 1

        return res