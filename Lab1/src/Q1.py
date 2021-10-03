import json
import timeit

f = open('Lab1\G.json',)
f1 = open('Lab1\Cost.json')
f2 = open('Lab1\Dist.json')
graph = json.load(f)
energycost = json.load(f1)
dist = json.load(f2)

visited = []
queue = []
predecessor = {}

def bfs(startnode, endnode):
    start_bfs = timeit.default_timer()
    visited.append(startnode)
    queue.append(startnode)
    predecessor[startnode]= [0,0]
    while queue:
        m = queue.pop(0)
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                temp = str(m)+','+str(neighbour)
                tempEnergy = energycost[temp]
                tempdist = dist[temp]
                predecessor[neighbour] = [m,tempdist]
                if neighbour == endnode:
                    stop_bfs = timeit.default_timer()
                    printshortestpath(endnode)
                    print('Time: ', stop_bfs - start_bfs)
                    return


def printshortestpath(endnode):
    shortestpath = []
    shortestpath.append(endnode)
    movement = endnode
    totaldist = 0
    while (predecessor[movement][0] != 0):
        shortestpath.insert(0, predecessor[movement][0])
        totaldist += predecessor[movement][1]
        movement = predecessor[movement][0]

    checkDist = 0
    energyCost = 0;
    print("Shortest Path: \nS -> ", end = '')
    for i in range(len(shortestpath)-1):
        print(shortestpath[i]+" -> ", end = '')
        a = shortestpath[i]
        b = shortestpath[i+1]
        temp1 = str(b)+','+str(a)
        checkDist += dist[temp1]
        energyCost += energycost[temp1]
    print(endnode+" -> T")
    print("\nShortest Distance: %.2f" % round(totaldist, 2))
    print("Total Energy Cost: "+str(energyCost))

# bfs('1','50')
