def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:

    n_features, n_observations = len(vectors), len(vectors[0])

    covariance_matrix = [[0 for _ in range(n_features)] for _ in range(n_features)]


    means = [sum(features)/n_observations for features in vectors]

    for i in range(n_features):
        for j in range(n_features):
            covariance = sum((vectors[i][k] - means[i])*(vectors[j][k] - means[i]) for k in range(n_observations))/ (n_observations - 1)
            covariance_matrix[i][j] = covariance
            covariance_matrix[j][i] = covariance

	return covariance_matrix