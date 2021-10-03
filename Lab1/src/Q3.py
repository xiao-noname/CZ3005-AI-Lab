import json
import math
import timeit
from queue import PriorityQueue

f = open('Lab1\G.json',)
f1 = open('Lab1\Cost.json')
f2 = open('Lab1\Dist.json')
f3 = open('Lab1\Coord.json')
graph = json.load(f)
energycost = json.load(f1)
dist = json.load(f2)
coord = json.load(f3)
predecessor = {}

# start = timeit.default_timer()


def linear_heuristic(currentNode, endNode):
    starting_x = coord[currentNode][0]
    starting_y = coord[currentNode][1]
    ending_x = coord[endNode][0]
    ending_y = coord[endNode][1]

    euclidean_distance = math.sqrt((starting_x - ending_x)**2 + (starting_y - ending_y)**2)
    return euclidean_distance

def updatedAStar (startnode,endnode):
    start_astar = timeit.default_timer()
    visited = set()
    q = PriorityQueue()
    predecessor[startnode] = 0
    for neighbour in graph[startnode]:
        temp1 = str(neighbour)+','+str(startnode)
        totalenergy = energycost[temp1]
        distNext = dist[temp1]
        heurDist = linear_heuristic(neighbour, endnode)
        functionDist = distNext + heurDist
        q.put((functionDist, (startnode, neighbour), totalenergy, distNext))
    while q:
        functionDist, (predecessornode, current), energy, traveldist = q.get()
        if current not in visited:
            visited.add(current)
            predecessor[current] = predecessornode
            if current == endnode:
                stop_astar = timeit.default_timer()
                printshortestpath(startnode, endnode)
                print('Time: ', stop_astar - start_astar)
                return
            for neighbours in graph[current]:
                temp = str(neighbours)+','+str(current)
                totalenergy = energy + energycost[temp]
                if neighbours not in visited and totalenergy <= 287932:
                    distNext = dist[temp]
                    heurDist = linear_heuristic(neighbours, endnode)
                    fdist = traveldist + distNext + heurDist
                    totaltravel = traveldist + distNext
                    # predecessor[neighbours] = current
                    q.put((fdist, (current, neighbours), totalenergy, totaltravel))


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

# updatedAStar('1','50')
