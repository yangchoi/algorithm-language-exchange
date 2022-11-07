class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    
        dict_ = {}
        for i in nums:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        return min(dict_, key=dict_.get)    