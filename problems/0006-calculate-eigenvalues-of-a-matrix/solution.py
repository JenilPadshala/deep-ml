import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

	a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]

	trace = a + d
	determinant = (a*d) - (b*c)

	discriminant = (trace)**2 - 4 * determinant
	solution = []
	if discriminant >= 0:
		discriminant_sqrt = math.sqrt(discriminant)
		lambda_1 = (trace + discriminant_sqrt) / 2.0
		lambda_2 = (trace - discriminant_sqrt) / 2.0
		solution = [lambda_1, lambda_2]
	return solution