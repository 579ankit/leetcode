class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        # Create (capital, profit) pairs
        projects = []
        for i in range(len(profits)):
            projects.append((capital[i], profits[i]))
        # Sort by capital required
        projects.sort()
        # Max heap (store negative profits)
        heap = []
        i = 0
        n = len(projects)
        while k > 0:
            # Add all projects that can be started
            while i < n and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1
            # No project can be started
            if not heap:
                break
            # Choose the project with maximum profit
            w += -heapq.heappop(heap)
            k -= 1
        return w