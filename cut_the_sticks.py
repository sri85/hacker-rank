# http://www.martinkysel.com/hackerrank-cut-the-sticks-solution/
#!/usr/bin/py
def computeSticks(arr):
    arr.sort(reverse=True)
    while len(arr) > 0:
        print len(arr)
        block_cut = arr.pop()
        while len(arr) > 0 and arr[-1] <= block_cut:
            arr.pop()
 
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    computeSticks(arr)
