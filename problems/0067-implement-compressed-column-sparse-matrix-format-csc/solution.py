import numpy as np
def compressed_col_sparse_matrix(dense_matrix):
	dense_matrix = np.array(dense_matrix)
	row, col = dense_matrix.shape
	vals = []
	row_idx = []
	col_ptr = [0]
	for j in range(col):
		for i in range(row):
			element = dense_matrix[i, j]
			if element != 0:
				vals.append(int(element))
				row_idx.append(int(i))
		col_ptr.append(int(len(vals)))
	return vals, row_idx, col_ptr