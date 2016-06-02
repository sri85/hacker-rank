# Problem Statement: https://www.hackerrank.com/challenges/pangrams
import string
sentence = raw_input().strip()
x = string.ascii_lowercase

y = ''.join(sorted(list(set((sentence.lower().replace(" ", ""))))))

if x == y:
    print "pangram"
else:
    print "not pangram"
