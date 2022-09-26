function reverseWords(s: string): string {
  const stringArr = s.split(' ');
  const newString: Array<string> = [];
  stringArr.forEach((str) => {
    const s = str.split('');
    let left = 0, right = str.length - 1;
    while (left < right) {
      [s[left], s[right]] = [s[right], s[left]];
      ++left;
      --right;
    }
    newString.push(s.join(''));
  });

  return newString.join(' ');
};