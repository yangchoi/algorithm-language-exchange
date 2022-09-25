function isIsomorphic(s: string, t: string): boolean {
  if (s.length !== t.length) return false;
  let sSet = new Set(s);
  let tSet = new Set(t);

  if (sSet.size !== tSet.size) {
    return false;
  }
  let map = new Map();

  for (let i = 0; i < s.length; i++) {
    if (map.has(s[i]) && map.get(s[i]) !== t[i]) {
      return false;
    } else {
      map.set(s[i], t[i]);
    }
  }
  return true;
};