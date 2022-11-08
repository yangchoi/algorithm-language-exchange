class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        dict_ = {}
        for i in nums:
            if i not in dict_:
                dict_[i] = 1
            else:
                dict_[i] += 1
        return min(dict_, key=dict_.get)

    def singleNumber2(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer = answer ^ num # ^ -> XOR
        return answer
        