import numpy as np
from scipy import stats
import math

def descriptive_statistics(data: list | np.ndarray) -> dict:
    mean = np.mean(data)
    median = np.median(data)
    m = stats.mode(data)
    if hasattr(m, 'mode'):
        mode_val = m.mode
    else:
        mode_val = m[0]
        
    if isinstance(mode_val, (np.ndarray, list, tuple)):
        mode = int(mode_val[0])
    else:
        mode = int(mode_val)
    variance = np.var(data)
    standard_deviation = math.sqrt(variance)
    q1 = np.percentile(data, 25)
    q2 = np.percentile(data, 50)
    q3 = np.percentile(data, 75)
    IQR = q3 - q1
    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'variance': variance,
        'standard_deviation': standard_deviation,
        '25th_percentile': q1,
        '50th_percentile': q2,
        '75th_percentile': q3,
        'interquartile_range': IQR
    }