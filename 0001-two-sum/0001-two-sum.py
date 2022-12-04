"""
approach
큰 for문을 돌면서 한 정수에 대해 다른 값들을 맞추어 가며 합이 taget이 되는지 확인한다.

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            dict = {}
            for i in range(len(nums)):
                if nums[i] in dict:
                    return [dict[nums[i]], i]
                else:
                    dict[target - nums[i]] = i



