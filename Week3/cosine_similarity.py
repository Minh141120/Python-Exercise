import numpy as np

def cosine_similarity(X, Y):
    dot_product = np.dot(X, Y)
    norm_X = np.linalg.norm(X)
    norm_Y = np.linalg.norm(Y)
    
    return dot_product / (norm_X * norm_Y)

X = np.array([1, 2, 3])
Y = np.array([4, 5, 6])

print(cosine_similarity(X, Y))