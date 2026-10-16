import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	dense_matrix = np.array(dense_matrix)
	values_array = []
	column_indices = []
	row_pointer = [0]
	row, column = dense_matrix.shape
	for i in range(row):
		for j in range(column):
			element = dense_matrix[i, j]

			if element != 0:
				values_array.append(int(element))
				column_indices.append(int(j))
		row_pointer.append(int(len(values_array)))

	return values_array, column_indices, row_pointer