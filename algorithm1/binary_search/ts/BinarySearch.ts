function search(nums: number[], target: number): number {
  if (!(nums.includes(target))) {
    return -1;
  }
  let result;
  nums.forEach((num) => {
    if (num === target) {
      result = nums.indexOf(num);
    }
  });
  return result;
};