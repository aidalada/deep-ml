import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float] | int:
    try: 
        result = np.dot(a, b)
        return result.tolist()  # Конвертируем массив numpy в обычный список Python
    except ValueError:
        return -1