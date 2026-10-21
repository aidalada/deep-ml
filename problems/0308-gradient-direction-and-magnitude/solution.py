import numpy as np
import math

def gradient_direction_magnitude(gradient: list) -> dict:
	gradient = np.array(gradient)
	sum_m = 0
	for num in gradient:
		sum_m += num ** 2
	magnitude = math.sqrt(sum_m)

	if magnitude == 0.0:
		direction = np.zeros_like(gradient, dtype=float)
        descent_direction = np.zeros_like(gradient, dtype=float)
	else:
		direction = gradient / magnitude
		descent_direction = -direction

	return {
        "magnitude": magnitude,
        "direction": direction,
        "descent_direction": descent_direction
    }