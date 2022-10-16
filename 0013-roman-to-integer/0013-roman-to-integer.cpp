class Solution {
public:
    int romanToInt(string s) {
      unordered_map<char, int> map = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
      int changed = 0;
      for(int idx = 0; idx < s.size(); ++idx) {
        if((idx < s.size() - 1) && (map[s[idx]] < map[s[idx + 1]])) {
          changed -= map[s[idx]];
        }else {
          changed += map[s[idx]];
        }
      }
      return changed;
    }
};