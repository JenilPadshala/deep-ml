
import numpy as np

def cosine_similarity(v1, v2):
	# Implement your code here
	dot_prod = v1 @ v2
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)

    return round(dot_prod / (norm_v1 * norm_v2), 3)
