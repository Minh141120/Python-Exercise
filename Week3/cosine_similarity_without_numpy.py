import math

def cosine_similarity(X, Y):
    dot_product = sum([x * y for x,  y in zip(X, Y)])
    norm_X = math.sqrt(sum([x ** 2 for x in X]))
    norm_Y = math.sqrt(sum([y ** 2 for y in Y]))
    return dot_product / (norm_X * norm_Y)
    
X = [1, 2, 3]
Y = [4, 5, 6]

print(cosine_similarity(X, Y))
