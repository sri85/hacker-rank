# Problem statement: https://www.hackerrank.com/challenges/diagonal-difference
T = int(input())
x = [map(int, raw_input().strip().split(" ")) for _ in range(T)]
primary_diagnol = []
for i in range(len(x)):
    primary_diagnol.append(x[i][i])
x.reverse()
secondary_diagnol = []
for j in range(len(x)):
    secondary_diagnol.append(x[j][j])

print abs(sum(primary_diagnol)-sum(secondary_diagnol))
