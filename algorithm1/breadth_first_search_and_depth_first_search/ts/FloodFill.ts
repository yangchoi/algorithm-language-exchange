function floodFill(
  image: number[][],
  sr: number,
  sc: number,
  newColor: number,
): number[][] {
  const DIRECTIONS = [
    [1, 0],
    [-1, 0],
    [0, -1],
    [0, 1],
  ]
  const targetColor = image[sr][sc]
  const stack = [[sr, sc]]

  if (newColor === image[sr][sc]) {
    return image
  }

  while (stack.length > 0) {
    const [x, y] = stack.pop()
    image[x][y] = newColor

    for (const [dx, dy] of DIRECTIONS) {
      if (image[x + dx] && image[x + dx][y + dy] === targetColor) {
        if (image[x + dx][y + dy] === targetColor) {
          stack.push([x + dx, y + dy])
        }
      }
    }
  }
  return image
}
