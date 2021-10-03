import json
import timeit
from queue import PriorityQueue

f = open('Lab1\G.json',)
f1 = open('Lab1\Cost.json')
f2 = open('Lab1\Dist.json')
graph = json.load(f)
energycost = json.load(f1)
dist = json.load(f2)

predecessor = {}


def ucs(startnode, endnode):
    start_ucs = timeit.default_timer()
    visited = set()
    q = PriorityQueue()
    predecessor[startnode] = 0
    # visited.add(startnode)
    # q.put((0,startnode,0))#predecessor,accumulatedEnergy
    for neighbour in graph[startnode]:
        temp1 = str(neighbour)+','+str(startnode)
        totalenergy = energycost[temp1]
        totaldist = dist[temp1]
        q.put((totaldist, (startnode, neighbour), totalenergy))
    while q:
        traveldist, (predecessornode, current), energy = q.get()
        if current not in visited:
            visited.add(current)
            predecessor[current] = predecessornode
            if current == endnode:
                stop_ucs = timeit.default_timer()
                printshortestpath(startnode, endnode)
                print('Time: ', stop_ucs - start_ucs)
                return
            for neighbours in graph[current]:
                temp = str(neighbours)+','+str(current)
                totalenergy = energy + energycost[temp]
                if neighbours not in visited and totalenergy <= 287932:
                    totaldist = dist[temp]+traveldist
                    predecessor[neighbours] = current
                    q.put((totaldist, (current, neighbours), totalenergy))


def printshortestpath(startnode, endnode):
    shortestpath = []
    shortestpath.append(endnode)
    movement = endnode
    while (predecessor[movement] != startnode):
        shortestpath.insert(0, predecessor[movement])
        movement = predecessor[movement]
    shortestpath.insert(0, startnode)

    totalDist = 0
    energyCost = 0
    print("Shortest Path: \nS -> ", end='')
    for i in range(len(shortestpath)-1):
        print(shortestpath[i]+" -> ", end='')
        a = shortestpath[i]
        b = shortestpath[i+1]
        temp1 = str(b)+','+str(a)
        totalDist += dist[temp1]
        energyCost += energycost[temp1]
    print(endnode+" -> T")
    print("\nShortest Distance: %.2f" % round(totalDist, 2))
    print("Total Energy Cost: "+str(energyCost))

# ucs('1','50')
