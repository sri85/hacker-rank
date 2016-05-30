# Problem Statement: https://www.hackerrank.com/challenges/sherlock-and-squares

from math import sqrt,floor
T = int(input())
for _ in range(T):
    x = map(int,raw_input().strip().split(" "))
    c = floor(sqrt(x[1]))- floor(sqrt(x[0]-1))
    print int(c)
