class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        a=[]
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                a.append(nums1[i])
                i+=1
            else:
                a.append(nums2[j])
                j+=1
        while i<m:
            a.append(nums1[i])
            i+=1
        while j<n:
            a.append(nums2[j])
            j+=1
        # copy back into nums1
        for k in range(len(a)):
            nums1[k] = a[k]