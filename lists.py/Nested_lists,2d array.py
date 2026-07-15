# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Access elements
print(matrix[0][0])  # 1
print(matrix[1][2])  # 6
print(matrix[2][1])  # 8

# Iterate through rows
for row in matrix:
    print(row)  # [1,2,3], [4,5,6], [7,8,9]

# Iterate through elements
for row in matrix:
    for element in row:
        print(element)  # 1, 2, 3, 4, 5, 6, 7, 8, 9

# Create 3x3 matrix of zeros
zeros = [[0] * 3 for _ in range(3)]
print(zeros)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Create identity matrix
identity = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print(identity)  # [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Matrix operations (transpose)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
