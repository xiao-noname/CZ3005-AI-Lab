import json
import timeit
from queue import PriorityQueue

G = open('.\data\G.json')
Cost = open('.\data\Cost.json')
Dist = open('.\data\Dist.json')

graph = json.load(G)
cost = json.load(Cost)
dist = json.load(Dist)

path = [0] * (len(graph) + 1)

def Task1(startNode, endNode):
    visited = [False] * (len(graph) + 1)

    queue = PriorityQueue()
    path[int(startNode)] = 0
    for neighbour in graph[startNode]:
        startNeighbour = str(neighbour) + ',' + str(startNode)
        totalenergy = cost[startNeighbour]
        totaldist = dist[startNeighbour]
        queue.put((totaldist, (startNode, neighbour), totalenergy))
    while queue:
        currentDistance, (lastNode, currentNode), currentEnergy = queue.get()
        currentNodeIndex = int(currentNode)
        if visited[currentNodeIndex]:
            continue
        visited[currentNodeIndex] = True
        path[currentNodeIndex] = lastNode
        if currentNode == endNode:
            printShortestPath(startNode,endNode)
            return
        for neighbour in graph[currentNode]:
            neighbourIndex = int(neighbour)
            currentNeighbour = str(neighbour)+','+str(currentNode)
            newEnergy = currentEnergy + cost[currentNeighbour]
            if not visited[neighbourIndex]:
                newDist = currentDistance + dist[currentNeighbour]
                path[neighbourIndex] = currentNode
                queue.put((newDist, (currentNode,neighbour), newEnergy))

def printShortestPath(startNode, endNode):
    shortestpath = []
    shortestpath.append(endNode)
    movement = endNode
    while (path[int(movement)] != startNode):
        shortestpath.insert(0, path[int(movement)])
        movement = path[int(movement)]
    shortestpath.insert(0, startNode)

    totalDist = 0
    energyCost = 0
    print("Shortest Path: \nS -> ", end='')
    for i in range(len(shortestpath)-1):
        print(shortestpath[i]+" -> ", end='')
        a = shortestpath[i]
        b = shortestpath[i+1]
        temp1 = str(b)+','+str(a)
        totalDist += dist[temp1]
        energyCost += cost[temp1]
    print(endNode+" -> T")
    print("\nShortest Distance: %.2f" % round(totalDist, 2))
    print("Total Energy Cost: "+str(energyCost))
    return
'''
print("|| Task 1: Breadth First Search ||")
start_time = timeit.default_timer()
Task1('1', '50')
end_time = timeit.default_timer()
print('Time: ', end_time - start_time)
'''
