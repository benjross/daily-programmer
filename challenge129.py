# link to problem:
# http://www.reddit.com/r/dailyprogrammer/comments/1hzq9y/071013_challenge_129_intermediate_ndimensional/

import math

def length(vector):
    return math.sqrt(sum(map(lambda x: math.pow(float(x), 2), vector[1:])))

def normalize(vector):
    l = length(vector)
    return ' '.join(map(lambda x: str(float(x) / l), vector[1:]))

def dot_product(vector1, vector2):
    return sum(map(lambda x, y: float(x) * float(y), vector1[1:], vector2[1:] ))

def do(method, vecs, vectors):
    vector1 = vectors[int(vecs[0])]
    vector2 = vectors[int(vecs[-1])]
    if method == "l":
        return length(vector1)
    elif method == "n":
        return normalize(vector1)
    else:
        return dot_product(vector1, vector2)

def parse():
    vectors = []
    num_vectors = int(raw_input())

    for i in range(num_vectors):
        vector = raw_input().split()
        vectors.append(vector)

    to_dos = int(raw_input())
    output = []

    for i in range(to_dos):
        to_do = raw_input().split()
        output.append(do(to_do[0], to_do[1:], vectors))

    for i in output:
        print i

parse()
