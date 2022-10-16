class Solution:
    def floodFill(self, image, sr, sc, newColor):
        color = image[sr][sc]
        if newColor == color:
            return color

        self.dfs(image, sr, sc, newColor, color)
        return image

    def dfs(self, image, r, c, newColor, color):
        m, n = len(image), len(image[0])
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        image[r][c] = newColor

        for d in directions:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == color:
                self.dfs(image, nr, nc, newColor, color)
