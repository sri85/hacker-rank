from datetime import date
d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]
d0 = date(y1, m1,d1)
d3 = date(y2, m2, d2)
delta = d0 - d3
days = delta.days
months = m1- m2
if days > 0:
    if y1 > y2:
        print 10000
    elif y1 == y2 and m1>m2:
        print months*500
    elif y1==y2 and m1 <=m2 and d1<=d2 and d1 >=d2:
        print 0
    elif y1==y2 and m1<=m2 and d1 >= d2:
        print days*15
    else:
        print 0
else:
    print 0

