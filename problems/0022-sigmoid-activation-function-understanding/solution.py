import math

def sigmoid(z: float) -> float:
	#Your code here
    Dr = 1 + math.exp(-z)
    result = round(1 / Dr, 4)
	return result