class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        heap = []
        results = [-1] * len(queries)
        intervals.sort(key=lambda x: x[0])
        # kolejność queries ma znaczenie -> zachowujemy indeks i wartość po której sortujemy 
        queries_sorted = sorted(enumerate(queries), key=lambda x: x[1])

        i = 0
        for orig_index, query in queries_sorted:
            while i < len(intervals) and intervals[i][0] <= query:
                begin, finish = intervals[i]
                heapq.heappush(heap, (finish-begin+1, finish))
                i += 1
                
            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            if heap:
                interval_length, interval_finish = heap[0]
                results[orig_index] = interval_length

        return results

