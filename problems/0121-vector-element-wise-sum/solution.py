import numpy as np
def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	a = np.array(a)
	b = np.array(b)

	if a.shape == b.shape:
		return a + b 
	else:
		return -1