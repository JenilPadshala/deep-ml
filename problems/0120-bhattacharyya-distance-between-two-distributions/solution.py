import numpy as np

def bhattacharyya_distance(p: list[float], q: list[float]) -> float:
    # Your code here

    if len(p) != len(q) or len(p) == 0 or len(q) == 0:
        return 0.0
    np_p = np.array(p)
    np_q = np.array(q)

    BC = np.sum(np.sqrt(np_p * np_q))

    BD = - np.log(BC)
    return np.round(BD, 4)