# Problem Statement: https://www.hackerrank.com/challenges/the-love-letter-mystery
T = int(input())
for _ in range(T):
    s = list(raw_input().strip())
    print(sum(abs(ord(s[i]) - ord(s[-i - 1])) for i in range(len(s) // 2)))
