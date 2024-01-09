class Solution:
    def floodFill(self, image: list, sr: int, sc: int, color: int) -> list:
        if sc < 0 or sr < 0 or color == image[sr][sc]:
            return image

        # Store the find value
        find = image[sr][sc]

        # Update current cell
        image[sr][sc] = color

        # Update up
        try:
            if image[sr - 1][sc] == find:
                image = self.floodFill(image, sr - 1, sc, color)
        except:
            pass
        
        # Update down
        try:
            if image[sr + 1][sc] == find:
                image = self.floodFill(image, sr + 1, sc, color)
        except:
            pass

        # Update right
        try:
            if image[sr][sc + 1] == find:
                image = self.floodFill(image, sr, sc + 1, color)
        except:
            pass

        # Update left
        try:
            if image[sr][sc - 1] == find:
                image = self.floodFill(image, sr, sc - 1, color)
        except:
            pass
            
        return image

def main():
    s = Solution()
    res = s.floodFill([[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2)

    print("Solution: ", res)

main()