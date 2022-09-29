function checkInclusion(s1: string, s2: string): boolean {
  const len1 = s1.length, len2 = s2.length;
  if (len1 > len2) return false;

  const count = Array(26);
  count.fill(0);
  for (let i = 0; i < len1; i++) {
    count[s1.charCodeAt(i) - 'a'.charCodeAt(0)]++;
    count[s2.charCodeAt(i) - 'a'.charCodeAt(0)]--;
  }

  if (allZero(count)) return true;

  for (let j = len1; j < len2; j++) { 
    count[s2.charCodeAt(j) - 'a'.charCodeAt(0)]--;
    count[s2.charCodeAt(j - len1) - 'a'.charCodeAt(0)]++;
    if (allZero(count)) return true;
  }
  return false;

};

function allZero(count: Array<number>): boolean {
  for (let i = 0; i < 26; i++) { 
    if (count[i] !== 0) return false;
  }
  return true;
}