class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        count = dict(Counter(nums1))
        
        for i in nums2:
            if i in count and count[i] != 0:
                    intersection.append(i)
                    count[i] = count[i] - 1
        return intersection