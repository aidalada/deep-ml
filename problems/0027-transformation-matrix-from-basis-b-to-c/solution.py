import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	B = np.array(B)
	C = np.array(C)

	det_C = np.linalg.det(C)
	inversed_C = np.linalg.inv(C)
	try:
		P = inversed_C @ B
		return P
	except ValueError:
		return -1
		
