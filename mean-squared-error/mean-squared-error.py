import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    if len(y_pred) != len(y_true):
        return None

    mse = float(np.mean ( (np.array(y_pred)-np.array(y_true))**2))

    return mse
