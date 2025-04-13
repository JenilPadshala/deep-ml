import numpy as np
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
    np_v = np.array(v)
    np_L = np.array(L)

    v_dot_L = np_v @ np_L
    L_dot_L = np_L @ np_L
    projection = (v_dot_L / L_dot_L) * np_L
    return projection.tolist()
