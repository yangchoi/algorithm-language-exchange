class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
      for(int i = digits.size() - 1; i >= 0; i--) {
        if(digits[i] < 9) {
          // 9미만일 경우엔 그냥 1을 더한다. 
          digits[i]++;
          return digits;
        }else {
          // 그렇지 않을 경우엔 0을 넣는다. 
          digits[i] = 0;
        }
      }
      // 9초과로 인해 여기로 온 값은 가장 뒤 값이 0으로 초기화가 된다. 
      digits.push_back(0);
      // 그리고 맨 앞의 값은 1이 된다. 
      digits[0] = 1;
      return digits;
    }
};