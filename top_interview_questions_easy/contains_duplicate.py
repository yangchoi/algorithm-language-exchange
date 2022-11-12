class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct_array = set(nums)
        if(len(nums) != len(distinct_array)):
            return True
        else:
            return False
        