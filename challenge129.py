# link to problem:
# http://www.reddit.com/r/dailyprogrammer/comments/1hzq9y/071013_challenge_129_intermediate_ndimensional/

def length():
    pass

def normalize():
    pass

def dot_product():
    pass

def do(method, vector1, vector2 = 0):
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
        output.append(do(to_do, vectors))

    print output

parse()
