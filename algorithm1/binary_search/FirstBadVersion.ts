/**
 * The knows API is defined in the parent class Relation.
 * isBadVersion(version: number): boolean {
 *     ...
 * };
 */

var solution = function(isBadVersion: any) {
  return function(n: number): number {
    let left = 0, right = n;

    while (left < right) {
      const middle = left + Math.floor((right - left)/2); // 중간지점

      if (isBadVersion(middle)) {
        right = middle;
        // minimum 체크하고 해당 지점 이전 탐색 
      } else {
        // 해당 지점 이후로 탐색
        left = middle + 1;
      }
      
    }
    return left;
  };  
};
