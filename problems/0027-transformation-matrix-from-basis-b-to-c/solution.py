import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:

    np_C = np.array(C)
    np_B = np.array(B)

    C_inv = np.linalg.inv(np_C)

    P = C_inv @ np_B
    return P.tolist()