import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'row':
		mode = 1
	elif mode == 'column':
		mode = 0

	matrix = np.array(matrix)
	result = matrix.mean(axis = mode)
	return result.tolist()