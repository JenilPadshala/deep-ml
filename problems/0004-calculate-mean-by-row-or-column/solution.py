def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    if mode == 'column':
        return [sum(matrix[row][col] for row in range(num_rows))/ num_rows for col in range(num_cols)]
    
    else:
        return [sum(row)/num_rows for row in matrix]