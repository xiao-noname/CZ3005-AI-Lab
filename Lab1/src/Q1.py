import json

f = open('Lab1\G.json',)
f1 = open('Lab1\Cost.json')
f2 = open('Lab1\Dist.json')
graph = json.load(f)
energycost = json.load(f1)
dist = json.load(f2)

visited = []
queue = []
predecessor = {}

def bfs(visited, graph,startnode, endnode):
    visited.append(startnode)
    queue.append(startnode)
    predecessor[startnode]= [0,0]
    while queue:
        m = queue.pop(0)
        #print(m, end = " ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                temp = str(m)+','+str(neighbour)
                tempEnergy = energycost[temp]
                tempdist = dist[temp]
                predecessor[neighbour] = [m,tempdist]
                if neighbour == endnode:
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

    print(shortestpath)         #change the way the print for project
    print(totaldist)


print("Following is the breadth-first search")
bfs(visited, graph, '1','50')
printshortestpath('50')