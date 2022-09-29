function floodFill(image: number[][], sr: number, sc: number, newColor: number): number[][] {
  if (image[sr][sc] !== newColor) {
    helper(image[sr][sc], newColor, sr, sr, image);
  };
  return image;
}; 

function helper(oldColor: number, newColor: number, r: number, c: number, image: number[][]) {
  image[r][c] = newColor;
  // left
  if (c - 1 >= 0 && image[r][c - 1] === oldColor) {
    helper(oldColor, newColor, r, c - 1, image);
  }
  // right 
  if (c + 1 < image[r].length && image[r][c + 1] === oldColor) {
    helper(oldColor, newColor, r, c + 1, image);
  }

  // top
  if (r - 1 >= 0 && image[r - 1][c] === oldColor) {
    helper(oldColor, newColor, r - 1, c, image);
  }

  // bottom
  if (r + 1 < image.length && image[r + 1][c] === oldColor) { 
    helper(oldColor, newColor, r + 1, c, image);
  }
  

}

/**
 * 1. 내가 선택한 index의 값을 target에 저장
 * 2. target과 newColor과 같은 경우 주어진 배열을 바로 반환. 
 *  : 위 경우에서 2로 바꾸는 것이 아닌 1로 바꾸는 것이라면 바꾸어도 원배열과 같기 때문에 의미가 없음
 * 3. 내가 선택한 index의 값을 newColor로 바꿔줌
 * 4. 선택한 index를 기준으로 유효한 인접 index 를 구함
 *  : up, down, left, right 구하는데 행렬 크기 고려해야함. 
 * 5. DFS 
 *  : 방문 여부는 newColor 로 변경되면서 자동적으로 체크됨
 * 6. 시작점 기준으로 출발
 */