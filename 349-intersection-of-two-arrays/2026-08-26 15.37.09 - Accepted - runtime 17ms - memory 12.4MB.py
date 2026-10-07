class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        list1=[]
        for i in nums1:
            if i in nums2:
                if i not in list1:
                    list1.append(i)
                   
        return list1