

def getMatrix(n,m,value):
   matrix = []
   for row in range(n):
      matrix.append([])
      for column in range(m):
         matrix[row].append(value)
   return matrix

print(getMatrix(2,2,10))