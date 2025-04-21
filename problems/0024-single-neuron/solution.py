import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	np_features = np.array(features)
    np_weights = np.array(weights)
    np_labels = np.array(labels)

    z = np.dot(np_features, np_weights) + bias
    sigmoid = lambda x: 1/ (1 + np.exp(-x))
    probabilities = np.round(sigmoid(z), 4)
    mse = round(np.sum((probabilities - np_labels)**2) / len(labels), 4)
	return probabilities.tolist(), mse