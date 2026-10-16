import numpy as np

def make_diagonal(x):
	x = np.array(x)
	matrix = np.diag(x)
	return matrix