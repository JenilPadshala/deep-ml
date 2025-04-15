import numpy as np 
from collections import Counter
def descriptive_statistics(data):
	# Your code here
	# stats_dict = {
    #     "mean": mean,
    #     "median": median,
    #     "mode": mode,
    #     "variance": np.round(variance,4),
    #     "standard_deviation": np.round(std_dev,4),
    #     "25th_percentile": percentiles[0],
    #     "50th_percentile": percentiles[1],
    #     "75th_percentile": percentiles[2],
    #     "interquartile_range": iqr
    # }
    mean = np.mean(data)
    median = np.median(data)

    counter = Counter(data)
    max_count = max(counter.values())
    modes = [val for val, count in counter.items() if count == max_count]
    mode = modes[0]
    
    variance = np.var(data)
    standard_deviation = np.std(data)
    q1 = np.percentile(data, 25)
    q2 = np.percentile(data, 50)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1

	return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'variance': np.round(variance, 4)