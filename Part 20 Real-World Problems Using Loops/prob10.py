# Transpose Matrix (ML)

matrix = [[1,2,3],[4,5,5]]
tranposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("Transposed Matrix:", tranposed_matrix)