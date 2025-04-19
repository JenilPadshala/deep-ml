import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here
	if seed is not None:
        np.random.seed(seed)
    
    indices = np.arange(len(X))
    np.random.shuffle(indices)

    X_shuffled = X[indices]
    y_shuffled = y[indices]

    return X_shuffled, y_shuffled