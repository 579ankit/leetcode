class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        freq={}
        low=high=0
        res=0
        for high in range(len(fruits)):
            freq[fruits[high]]=freq.get(fruits[high],0)+1
            while len(freq)>2:
                freq[fruits[low]]-=1
                if freq[fruits[low]]==0:
                    del freq[fruits[low]]
                low+=1
            length=high-low+1
            res=max(res,length)
        return res
