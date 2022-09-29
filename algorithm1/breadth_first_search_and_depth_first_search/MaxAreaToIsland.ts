function maxAreaOfIsland(grid: number[][]): number {
  let rows = grid.length;
  let columns = grid[0].length;

  let maxArea = 0;
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < columns; j++) {
      if (grid[i][j] === 1) {
        maxArea = Math.max(dfs(grid, i, j), maxArea);
      }
    }
  }
  return maxArea;
};

function dfs(grid: number[][], i: number, j: number): number {
  let totalArea = 0;
  if ((i >= 0 && i < grid.length) && (j >= 0 && j < grid[0].length) && grid[i][j] === 1) { 
    grid[i][j] = 0;
    totalArea++;

    totalArea += dfs(grid, i + 1, j);
    totalArea += dfs(grid, i - 1, j);
    totalArea += dfs(grid, i, j + 1);
    totalArea += dfs(grid, i, j - 1);
  }
  return totalArea;
}