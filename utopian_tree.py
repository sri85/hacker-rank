# Problem Statement: https://www.hackerrank.com/challenges/utopian-tree
t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(input())
    tree_height = 1
    for i in range(n):
        if i%2==0:
            tree_height*=2
        else:
            tree_height+=1
    print tree_height
