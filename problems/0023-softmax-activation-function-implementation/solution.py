import math

def softmax(scores: list[float]) -> list[float]:
	# Your code here
    exp_values = [math.exp(z) for z in scores]
    total = sum(exp_values)

    probabilities = [round(z /total, 4) for z in exp_values ]
	return probabilities