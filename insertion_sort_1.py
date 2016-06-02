# Problem Statement: https://www.hackerrank.com/challenges/insertionsort1
def insertionSort(l):    
    list_length = len(l)
    for i in range(list_length):
        val = l[i]
        hole = i
        while hole > 0 and l[hole-1] > val:
            l[hole] = l[hole-1]
            hole -= 1
            temp = map(str,l)
            print " ".join(temp)
        l[hole] = val

    x = map(str,l)
    return " ".join(x)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
print insertionSort(ar)
