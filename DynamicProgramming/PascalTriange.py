from typing import List

class Solution:
    def __init__(self):
      self.PascalTriangle = []
      
    def generate(self, numRows: int) -> List[List[int]]:
      """
      1 1 1 1 1
      1 2 3 4 N
      1 3 6 N N
      1 4 N N N
      1 N N N N
      """
      for index in range(1, numRows+1):
        self.addRow()
      
    def addRow(self) -> None:
      rows = len(self.PascalTriangle)
      
      if rows == 0:
        self.PascalTriangle.append([1])
        return
      
      if rows == 1:
        self.PascalTriangle.append([1,1])
        return
        
      row = self.PascalTriangle[-1]
      nextRow = [1]
      
      for index in range(1, len(row)):
        nextRow.append(row[index - 1] + row[index])
        
      nextRow.append(1)
      
      self.PascalTriangle.append(nextRow)
      
if __name__ == "__main__":
  s = Solution()
  s.generate(5)
  print(s.PascalTriangle)