import numpy as np
import math

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
	if degree < 0:
		return []

	transformed = []
	for x in data:
		transformed.append([x ** p for p in range(degree + 1)])

	return transformed