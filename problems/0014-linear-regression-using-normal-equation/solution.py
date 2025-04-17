import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round

	np_X = np.array(X)
	np_y = np.array(y)

	theta = np.linalg.inv(np_X.T @ np_X) @ np_X.T @ np_y

	return [round(val, 4)for val in theta.tolist()]