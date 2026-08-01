import heapq

class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

class Solution(object):
    def topKFrequent(self, words, k):
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        heap = []
        for word, count in freq.items():
            heapq.heappush(heap, Word(count, word))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []
        while heap:
            ans.append(heapq.heappop(heap).word)
        return ans[::-1]