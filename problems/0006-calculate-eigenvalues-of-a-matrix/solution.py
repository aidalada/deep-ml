import numpy as np
from numpy import linalg as LA
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	matrix = np.array(matrix)
	eigenvalues, eigenvectors = LA.eig(matrix)
	return eigenvalues.real.tolist()
