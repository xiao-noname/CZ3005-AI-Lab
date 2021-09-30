import json
from queue import PriorityQueue

f = open('G.json',)
f1 = open('Cost.json')
f2 = open('Dist.json')
f3 = open('Coord.json')
graph = json.load(f)
energycost = json.load(f1)
dist = json.load(f2)
coord = json.load(f3)
predecessor = {}


def linear_heuristic(currentNode, endNode):  # euclidean_distance
    starting = coord[currentNode]
    ending = coord[endNode]
    euclidean_distance = math.sqrt(
        (starting[0] - ending[0])**2 + (starting[1] - ending[1])**2)
    temp1 = str(endNode)+','+str(currentNode)
    return euclidean_distance


def updatedAStar(startnode, endnode):
    visited = set()
    q = PriorityQueue()
    predecessor[startnode] = 0
    for neighbour in graph[startnode]:
        temp1 = str(neighbour)+','+str(startnode)
        totalenergy = energycost[temp1]
        heurDist = linear_heuristic(startnode, endnode)/11
        totaldist = dist[temp1] + heurDist
        q.put((totaldist, (startnode, neighbour), totalenergy, heurDist))
    while q:
        traveldist, (predecessornode, current), energy, hdist = q.get()
        if current not in visited:
            visited.add(current)
            predecessor[current] = predecessornode
            if current == endnode:
                return
            for neighbours in graph[current]:
                temp = str(neighbours)+','+str(current)
                totalenergy = energy + energycost[temp]
                if neighbours not in visited and totalenergy <= 287932:
                    heurDist = linear_heuristic(startnode, endnode)/11
                    totaldist = dist[temp]+traveldist+heurDist-hdist
                    predecessor[neighbours] = current
                    q.put((totaldist, (current, neighbours), totalenergy, heurDist))


def printshortestpath(startnode, endnode):
    shortestpath = []
    shortestpath.append(endnode)
    movement = endnode
    while (predecessor[movement] != startnode):
        shortestpath.insert(0, predecessor[movement])
        movement = predecessor[movement]
    shortestpath.insert(0, startnode)
    print("This is the length of the shortest path " + str(len(shortestpath)))
    checkDist = 0
    for i in range(len(shortestpath)-1):
        a = shortestpath[i]
        b = shortestpath[i+1]
        temp1 = str(b)+','+str(a)
        checkDist += dist[temp1]
    print("The total distance of this function is: "+str(checkDist))


ucs('1', '50')
updatedAStar('1', '50')
printshortestpath('1', '50')
