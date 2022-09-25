function moveZeroes(nums: number[]): void {
  if (nums.includes(0)) {
    for (let i = nums.length - 1; i >= 0 - 1; --i) {
      if (nums[i] === 0) {
        nums.splice(i, 1);
        nums.push(0);
      }
    }
  }
}