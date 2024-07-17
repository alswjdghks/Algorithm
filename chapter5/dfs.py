
#def dfs(graph,v,visited):
#    visited[v] = True
#    print(v,end=' ')
#    for i in graph[v]:
#        if not visited[i]:
#            dfs(graph,i,visited)
#dfs(graph,1,visited)

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited = [False] * 9
stack = []
def stackDfs(graph,v,stack,visited):
    visited[v] = True
    stack.append(v)
    while stack:
        i = stack.pop()
        print(i,end=' ')
        for j in graph[i]:
            if visited[j] == False:
                stack.append(j) 
                visited[j] = True
stackDfs(graph,1,stack,visited)