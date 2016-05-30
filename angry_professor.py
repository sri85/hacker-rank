# Problem Statement: https://www.hackerrank.com/challenges/angry-professor
T = int(input())
for _ in xrange(T):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    c = 0
    for i in a:
        if i <= 0:
            c += 1
    if c < k:
        print "YES"
    else:
        print "NO"
