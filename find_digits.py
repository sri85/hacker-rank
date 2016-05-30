# Problem Statement: https://www.hackerrank.com/challenges/find-digits
T = int(input())
for _ in range(T):
    n = str(input())
    list_n = list(n)
    c = 0
    for i in list_n:
        try:
            if int(n) % (int(i)) == 0:
                c += 1
        except:
                pass
    print c
