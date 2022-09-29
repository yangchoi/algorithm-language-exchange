function lengthOfLongestSubstring(s: string): number {
  let biggestList = 0;
  let visitedNumber: { [p: string]: number } = {}; // value is the index
  let start = 0;

  for (let end = 0; end < s.length; end++) {
    while (visitedNumber[s[end]]) {
      delete visitedNumber[s[start]];
      start += 1;
    }

    visitedNumber[s[end]] = 1;
    biggestList = Math.max(biggestList, end - start + 1);
  }
  return biggestList;
}; 