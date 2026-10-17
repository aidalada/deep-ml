import numpy as np
def orthogonal_projection(v, L):
	v = np.array(v)
	L = np.array(L)
	try:
		mult1 = v @ L
		mult2 = L @ L
		deviation = mult1 / mult2
		result = deviation * L
		return result.tolist()
	except ValueError:
		return -1
		