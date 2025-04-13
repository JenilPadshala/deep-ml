def compressed_col_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	rows = len(dense_matrix)
    cols = len(dense_matrix[0])

    vals = []
    row_idx = []
    cols_ptr = []
    for j in range(cols):
        for i in range(rows):
            if dense_matrix[i][j] != 0:
                vals.append(dense_matrix[i][j])
                row_idx.append(i)
                cols_ptr.append(j)
    return vals, row_idx, cols_ptr

