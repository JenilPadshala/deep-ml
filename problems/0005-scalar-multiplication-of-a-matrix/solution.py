def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	return [matrix[row][col]*scalar for row in range(len(matrix)) for col in range(len(matrix[0]))]