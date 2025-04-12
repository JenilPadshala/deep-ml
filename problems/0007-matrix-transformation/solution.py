import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

	np_A = np.array(A)
	np_T = np.array(T)
	np_S = np.array(S)

	det_T = np.linalg.det(np_T)
	det_S = np.linalg.det(np_S)
	
	if det_T==0 or det_S==0:
		return -1
	
	np_T_inv = np.linalg.inv(np_T)

	sol = np_T_inv @ np_A @ np_S
	return sol.tolist()
