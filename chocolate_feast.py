# Problem statement: https://www.hackerrank.com/challenges/chocolate-feast
T = int(input())
for _ in xrange(T):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    total = wrappers = n / c;

    while wrappers >= m:
	 
        trade = wrappers / m
        total +=  trade
        wrappers = wrappers % m
        wrappers +=  trade

    print total
