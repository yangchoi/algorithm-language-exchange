class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
      if(nums.size() == 0) return 0;

      int init = 1;
      for(auto i = 1; i < nums.size(); ++i) {
        if(nums[i] != nums[i-1]) {
          nums[init] = nums[i];
          init++;
        }
      }
      return init;
    }
};