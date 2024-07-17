loc = input()
col = int(ord(loc[0]) - ord('a')) + 1
row = int(loc[1])

count = 0
step_type = [(2,1) , (2,-1) , (-2,1) , (-2,-1) , (1,2) , (1,-2) , (-1,2) , (-1,-2) ]
for step in step_type:
    if 1 <= col + step[1] <= 8 and 1 <= row + step[0] <= 8:
        count += 1
print(count)