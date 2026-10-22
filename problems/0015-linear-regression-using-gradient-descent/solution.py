import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:

    m, n = X.shape
    y = y.reshape(-1, 1)  
    theta = np.zeros((n, 1))  

    for _ in range(iterations):
        y_head = np.dot(X, theta)
        errors = y_head - y
        g = (1 / m) * np.dot(X.T, errors)
        theta = theta - alpha * g
    return theta.flatten()