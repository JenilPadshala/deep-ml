import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	rows = len(dense_matrix)
    cols = len(dense_matrix[0])
    v = []
    c = []
    r = []
    non_zero_counter = 0
    for i in range(rows):
        r.append(non_zero_counter)
        for j in range(cols):
            if dense_matrix[i][j] != 0:
                non_zero_counter += 1
                v.append(dense_matrix[i][j])
                c.append(j)
    r.append(non_zero_counter)
    return v,c,r


