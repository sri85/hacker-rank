# https://www.hackerrank.com/challenges/time-conversion

time = raw_input().strip()
t = datetime.strptime(time,"%I:%M:%S%p")
print str(t).split(" ")[1]
