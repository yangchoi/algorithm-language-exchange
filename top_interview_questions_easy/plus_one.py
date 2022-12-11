  """
  # approach
  마지막 index 리스트를 찾는다.
  해당 인덱스에 1을 더하고 해당 요소가 10이 넘을 경우 올림 수를 저장하고
  바로 앞 요소에 더한다.

  # answer
  리스트를 문자로 바꾼 다음 join()을 이용해 문자열로 합쳐준다.
  합쳐준 문자열을 숫자로 바꾼 다음 +1
  그런 후 문자열로 바꾸어 리스트로 만들어 반환
  """
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))
        nums = int(''.join(digits))
        nums += 1
        nums = list(str(nums))
        return list(map(int, nums))

