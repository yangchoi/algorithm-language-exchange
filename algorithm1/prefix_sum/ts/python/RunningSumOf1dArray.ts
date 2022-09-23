function runningSum(nums: number[]): number[] {
  let result: Array<number> = []
  let currValue = 0;
  nums.forEach((v) => {
    currValue = currValue + v;
    result.push(currValue);
  })
  return result;
};