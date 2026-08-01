class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        n=len(nums)
        # Put last k elements into heap
        for i in range(n-1,n-k-1,-1):
            heapq.heappush(heap, nums[i])
        
        # Process remaining elements
        for i in range(n-k-1,-1,-1):
            if nums[i] >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])

        return heap[0]