import numpy as np

def euclidean_distance(a,b):
    return np.sqrt(((a-b)**2).sum(axis=1))

def k_means_clustering(points: list[tuple[float, float]], k: int, initial_centroids: list[tuple[float, float]], max_iterations: int) -> list[tuple[float, float]]:
    points = np.array(points)
    centroids = np.array(initial_centroids)

    for _ in range(max_iterations):
        # 1. calculate distance of each point from each centroid
        distances = np.array([euclidean_distance(points, centroid) for centroid in centroids])

        # 2. assign each point to the closest centroid
        assignments = np.argmin(distances, axis=0)

        # 3. calculate the new centroids
        new_centroids = np.array([points[assignments == i].mean(axis=0) if len(points[assignments == i]) > 0 else centroids[i] for i in range(k)])

        # 4. check for convergence 
        if np.all(centroids == new_centroids):
            break
        
        centroids = new_centroids
        centroids = np.round(cen