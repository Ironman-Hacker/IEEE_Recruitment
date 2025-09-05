import numpy as np
matrix = np.random.randint(1, 101, size=(5, 5))
print(matrix)
middle = matrix[1:4, 1:4]
print(middle)
row = middle[0, :]
col = middle[:, -1]
print(row)
print(col)
dot_product = np.dot(row, col)
print(dot_product)
