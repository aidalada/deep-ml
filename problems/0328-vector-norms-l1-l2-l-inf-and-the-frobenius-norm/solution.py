import numpy as np
import math
def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    norms = ['l1', 'l2', 'linf', 'frobenius']
    sum = 0

    if norm_type in ['frobenius'] and arr.ndim != 2:
        raise ValueError("Array must be 2D for this norm.")

    if norm_type in norms:
        if norm_type == 'l1':
            arr = abs(arr)
            return float(arr.sum())
        elif norm_type == 'l2':
            arr = abs(arr)
            arr = arr ** 2
            return float(math.sqrt(arr.sum()))
        elif norm_type == 'linf':
            arr = abs(arr)
            return float(arr.max())
        elif norm_type == 'frobenius':
            arr = abs(arr)
            arr = arr ** 2
            return float(math.sqrt(arr.sum()))
        else:
            raise ValueError('Unknown norm type')
            
