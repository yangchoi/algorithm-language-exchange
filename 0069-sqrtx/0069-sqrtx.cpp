class Solution {
public:
    int mySqrt(int x) {
      int low = 0, high = x, mid;
      if(x < 2) return x; // mid가 0이 되면 안되므로 
      while(low < high) {
        mid = (low + high)/2;
        if(x/mid >= mid) {
          low = mid + 1;
        }else {
          high = mid;
        }
      }
      return high - 1;


    }
};