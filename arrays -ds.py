# Problem link: https://www.hackerrank.com/challenges/arrays-ds/copy-from/21294107

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print " ".join(map(str,arr[::-1]))
