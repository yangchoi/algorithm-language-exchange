class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
      unordered_map<int, int> map;
      for(int i = 0; i < nums.size(); ++i) {
        if(map.find(target - nums[i]) != map.end()) {
          return {map[target - nums[i]], i};
        }
      map.insert({nums[i], i});
      }
      return {};
    }
};

// unordered_map
// 원소들이 순서대로 정렬되어 들어가지 않음
// 삽입, 삭제, 조회가 평균 O(1)을 보장(최악의 경우 O(N))
// 해시 함수 사용해 저장공간 결정
// 너무 빈번하게 자료 삽입, 삭제하지 않고 많은 자료저장 및 빠른 검색 속도를 원할 때 사용