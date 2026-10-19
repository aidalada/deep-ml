import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    matrix = np.array(vectors)
    if matrix.ndim == 1:
        return True
        
    if matrix.ndim != 2:
        return False
        
    num_vectors = matrix.shape[0]
    rank = np.linalg.matrix_rank(matrix)
    
    return rank == num_vectors