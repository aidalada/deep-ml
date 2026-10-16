import numpy as np

def matrixmul(a: list[list[int | float]], b: list[list[int | float]]) -> list[list[int | float]] | int:
    try:
        c = np.matmul(a, b)
        return c.tolist()
    except ValueError:
        return -1