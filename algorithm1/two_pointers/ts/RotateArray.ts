/**
 Do not return anything, modify nums in-place instead.
 */
 function rotate(nums: number[], k: number): void {
  if(k !== 0) {
    if(k < nums.length) {
      const slicedArray = nums.slice(nums.length - k, nums.length);
      nums.splice(nums.length - k, k);
      nums.unshift(...slicedArray);
    }else {
      for(let count = 1; count <= k; count++){
        nums.unshift(nums.pop());
      }
    }
  };
};


function rotate2(nums: number[], k: number) {
  for (let i = 0; i < k; i++) {
    nums.unshift(nums.pop());
  }
}
// unshift : 가장 앞에 배열을 붙임
// pop: 가장 뒤의 요소를 제거