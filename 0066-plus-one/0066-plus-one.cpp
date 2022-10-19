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
        digits.push_back(0);
        digits[0] = 1;
        return digits;
    }
};