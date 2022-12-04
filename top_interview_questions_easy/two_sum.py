
class Solution:
    """
    approach
    큰 for문을 돌면서 한 정수에 대해 다른 값들을 맞추어 가며 합이 target이 되는지 확인한다.

    fail
    i + 1 과 같이 임의로 증가시킨 index 가 range out 이 되어 버린다.

    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] + nums[j] == target:
                          return [i, j]

    """
    success code
    hash_table을 사용한다.
    nums 를 돌면서 nums[i]를 hash_table에 넣는다.
    이후 해당 hash_table에는 nums[i]와 더하면 target이 나오는 값, 즉 target - nums[i]가 들어간다.
    """
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return [hash_table[nums[i]], i]
            else:
                hash_table[target-nums[i]] = i



