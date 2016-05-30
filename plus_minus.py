# Problem Statement: https://www.hackerrank.com/challenges/plus-minus


T = int(input())
x = map(int, raw_input().strip().split(" "))
positive = []
negative = []
zero = []
for i in x:
    if i > 0:
        positive.append(i)
    elif i < 0:
        negative.append(i)
    else:
        zero.append(i)
print round(len(positive)/float(T),6)
print round(len(negative)/float(T),6)
print round(len(zero)/float(T),6)
