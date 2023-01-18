def dijkstra(n,g):
    visited=[]
    cost=[999999 for i in range(n)]
    cost[0]=0
    min_cost = min(cost)
    vertex = cost.index(min(cost))
    for i in range (n-1):
        if vertex not in visited:
            visited.append(vertex)
            print(vertex)
            for j in range (n):
                if (g[vertex][j] != 0 and min_cost+g[vertex][j]<cost[j]):
                    cost[j] = min_cost+g[vertex][j]
        min_cost = 999999
        for i in range (n):
            if i not in visited:
                if cost[i] < min_cost:
                    min_cost = cost[i]
        vertex = cost.index(min_cost)
        print(cost)

n = 6
g = [[0,10,0,0,0,8],
     [0,0,1,2,0,0],
     [0,0,0,0,0,0],
     [0,0,-2,0,0,0],
     [0,-4,0,-1,0,0],
     [0,0,0,0,1,0]]

dijkstra(n,g)