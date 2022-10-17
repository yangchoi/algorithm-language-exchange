class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
      if(strs.size() == 0 ) return "";
      // strs을 사전식으로 정렬
      sort(strs.begin(), strs.end());
      // 그 중 첫번째와 마지막 문자를 가져옴
      string frontString = strs[0], lastString = strs[strs.size() - 1], result = "";
      // 각 string 배열의 길이를 가져옴
      int frontSize = frontString.size(), lastSize = lastString.size();
      
      // 0부터 시작해서 frontSize와 lastSize보다 i가 작을 동안
      // 앞부터 차례대로 가져오는 frontString과, 뒤에서 차례로 가져오는 lastString을 비교하여 
      // 같을 경우 result에 front[i] 해당 문자를 삽입
      for(int i = 0; i < frontSize && i < lastSize && frontString[i] == lastString[i]; i++) {
        result += frontString[i];
      }
      return result;
    }
};