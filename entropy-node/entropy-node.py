import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if len(y) == 0:
        return 0.0
    res, counts = np.unique(y, return_counts=True)
    total = len(y)
    entpy = 0
    for i in range (len(res)):
        pr = counts[i]/total

    # pra = counts[0]/total
    # prb = counts[1]/total
        entpy += -pr*np.log2(pr)

    return entpy