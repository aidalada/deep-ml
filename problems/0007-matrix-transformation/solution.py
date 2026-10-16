import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A = np.array(A)
	T = np.array(T)
	S = np.array(S)

	det_T = np.linalg.det(T)
	det_S = np.linalg.det(S)
	if det_T != 0 and det_S != 0:
		inversed_T = np.linalg.inv(T)
		try:
			init_transformed_matrix = inversed_T @ A
			transformed_matrix = init_transformed_matrix @ S
			return transformed_matrix
		except ValueError:
			return -1
	else:
		return -1