class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        # Build frequency map
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        # Build max heap
        heap = []
        for ch, count in freq.items():
            heapq.heappush(heap, (-count, ch))
        res = []
        prev_count = 0
        prev_char = ""

        while heap:
            count, ch = heapq.heappop(heap)
            res.append(ch)
            # Push previous character back if it still has remaining frequency
            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))
            # One occurrence used
            count += 1
            # Save current character
            prev_count = count
            prev_char = ch
        if len(res) != len(s):
            return ""
        return "".join(res)