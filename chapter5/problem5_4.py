from collections import deque
n,m = map(int,input().split())

miro = []
for i in range(n):
    miro.append(list(map(int,input())))

col = [0,0,1,-1]
row = [-1,1,0,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + row[i]
            ny = y + col[i]
            if nx<0 or nx >= n or ny < 0 or ny >= m :
                continue
            if miro[nx][ny] == 0:
                continue
            if miro[nx][ny] == 1:
                queue.append((nx,ny))
                miro[nx][ny] = miro[x][y] + 1
    return miro[n-1][m-1]

print(bfs(0,0))
    

