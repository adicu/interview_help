# Find the Euclidean distance between 2 points in n dimensions.

def distance(x,y):
  square_sum = 0
  for i in range(len(x)):
     square_sum += pow(x[i] - y[i], 2)
  return sqrt(square_sum)
