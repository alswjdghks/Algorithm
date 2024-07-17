n,m = map(int,input().split())

d = [ [0] * m for _ in range (n)]
x,y,direction = map(int,input().split())
d[x][y] = 1

print("draw map")
Map = []
for i in range(n):
    Map.append(list(map(int,input().split())))


row = [-1,0,1,0] 
col = [0,1,0,-1] 
  
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + row[direction]
    ny = y + col[direction]
    if d[nx][ny] == 0 and Map[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - row[direction]
        ny = y - col[direction]
        if Map[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)
