# link to problem:
# http://www.reddit.com/r/dailyprogrammer/comments/1i65z6/071213_challenge_126_hard_notsonormal_triangle/



# For a convex polygon (such as a triangle), a surface normal can be calculated as the vector cross product of two (non-parallel) edges of the polygon.

def length(edge):
	return math.sqrt(sum(map(lambda  x: float(x) ** 2, edge)))

def cross(triangle):
	return length(triangle[0:2]) * length(triangle[1:3]) *

def parse():
    triangles = []
    num_triangles = int(raw_input())

    for i in range(num_triangles):
        triangle = raw_input().split()
        triangles.append(triangle)

    vector = raw_input().split()

    output = []

    for i in range(to_dos):
        to_do = raw_input().split()
        output.append(do(to_do[0], to_do[1:], triangles))

    for i in output:
        print i

parse()
