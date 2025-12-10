# mean_var_std.py
import numpy as np


def calculate(input_list):
    # Check if exactly 9 numbers
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert list to 3x3 NumPy array
    arr = np.array(input_list).reshape(3, 3)

    # Compute all statistics
    result = {
        'mean': [
            np.mean(arr, axis=0).tolist(),  # mean of columns (axis=0)
            np.mean(arr, axis=1).tolist(),  # mean of rows (axis=1)
            np.mean(arr)  # mean of flattened
        ],
        'variance': [
            np.var(arr, axis=0).tolist(),
            np.var(arr, axis=1).tolist(),
            np.var(arr)
        ],
        'standard deviation': [
            np.std(arr, axis=0).tolist(),
            np.std(arr, axis=1).tolist(),
            np.std(arr)
        ],
        'max': [
            np.max(arr, axis=0).tolist(),
            np.max(arr, axis=1).tolist(),
            np.max(arr)
        ],
        'min': [
            np.min(arr, axis=0).tolist(),
            np.min(arr, axis=1).tolist(),
            np.min(arr)
        ],
        'sum': [
            np.sum(arr, axis=0).tolist(),
            np.sum(arr, axis=1).tolist(),
            np.sum(arr)
        ]
    }

    return result