function pivotIndex(nums: number[]): number {
  let rightSum = nums.reduce((a, b) => a + b);
  let leftSum = 0;
  

  for (let i = 0; i < nums.length; i++) {
    rightSum -= nums[i];
    if (leftSum === rightSum) {
      return i;
    }
    leftSum += nums[i];
  }
  return -1;

};