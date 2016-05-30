#Problem:https://www.hackerrank.com/challenges/2d-array
arr_2d = [[0 for x in range(6)] for x in range(6)]
for j in range(0,6):
    arr = [int(i) for i in raw_input().strip().split()]
    for k in range(0,6):
        arr_2d[j][k] = arr[k] 

maximum_value = -100        
for i in range(0,4):
    for j in range(0,4):
        count = 0
        count = arr_2d[i][j] + arr_2d[i][j+1] + arr_2d[i][j+2] + arr_2d[i+1][j+1] + arr_2d[i+2][j] + arr_2d[i+2][j+1] + arr_2d[i+2][j+2]
        if(count >= max_val):
            maximum_value = count
        
print maximum_value
