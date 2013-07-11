# link to problem:
# http://www.reddit.com/r/dailyprogrammer/comments/1hvh6u/070813_challenge_132_easy_greatest_common_divisor/


def gcd(first, second):
    for i in range (first, 0, -1):
        if first % i == 0 and second % i == 0:
            return i

def gcd_euclid(first, second):
    if not (first and  second):
        return first + second
    return gcd_euclid(second, first - second*(first / second))

print(gcd(32, 12))
print(gcd(142341, 512345))
print(gcd(65535, 4294967295))

print(gcd_euclid(32, 12))
print(gcd_euclid(142341, 512345))
print(gcd_euclid(65535, 4294967295))
