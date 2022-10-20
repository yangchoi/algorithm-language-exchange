class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
      if(n == 0) return;

      vector<int> mergedList;
      int index1 = 0, index2 = 0;

      while(index1 < m || index2 < n) {
        if(index1 < m && index2 < n) {
          if(nums1[index1] <= nums2[index2]) {
            mergedList.push_back(nums1[index1]);
            ++index1;
          }else {
            mergedList.push_back(nums2[index2]);
            ++index2;
          }
        }else if(index1 < m) {
          mergedList.push_back(nums1[index1]);
          ++index1;
        }else if(index2 < n) {
          mergedList.push_back(nums2[index2]);
          ++index2;
        }
      }

      for(int i = 0; i < m+n; i++) {
        nums1[i] = mergedList[i];
      }

    }

};