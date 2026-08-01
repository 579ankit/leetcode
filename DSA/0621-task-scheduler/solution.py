class Solution:
    def leastInterval(self, tasks, n):
        # Frequency map
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        # Max heap
        heap = []
        for count in freq.values():
            heapq.heappush(heap, -count)
        cooling = {}
        time = 0
        while heap or cooling:
            time += 1
            # Tasks whose cooldown is finished
            if time in cooling:
                for count in cooling[time]:
                    heapq.heappush(heap, -count)
                del cooling[time]
            # Execute one task
            if heap:
                count = -heapq.heappop(heap)
                count -= 1
                if count > 0:
                    ready_time = time + n + 1

                    if ready_time not in cooling:
                        cooling[ready_time] = []
                    cooling[ready_time].append(count)
        return time