# 253. Meeting Rooms II
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        heap = []
        
        intervals.sort()
        
        heappush(heap, intervals[0][1])
        
        for i in intervals[1:]:
            
            if heap[0] <= i[0]:
                heappop(heap)
            heappush(heap, i[1])
        return len(heap)
        
        
