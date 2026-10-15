import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    matrix = np.array(matrix)
    a = matrix[0,0]
    b = matrix[0, 1]
    c = matrix[1, 0]
    d = matrix[1, 1]
    det_A = np.linalg.det(matrix)
    if det_A != 0:
        inverse_matrix = (1 / det_A) * np.array([
            [d, -b],
            [-c, a]
        ])
    else:
        return None

    return inverse_matrix
