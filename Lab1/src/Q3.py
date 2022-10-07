import json
import math
import timeit
from queue import PriorityQueue

f = open('/Users/xiaolingyi/Documents/GitHub/CZ3005-AI-Lab/Lab1/G.json',)
f1 = open('/Users/xiaolingyi/Documents/GitHub/CZ3005-AI-Lab/Lab1/Cost.json')
f2 = open('/Users/xiaolingyi/Documents/GitHub/CZ3005-AI-Lab/Lab1/Dist.json')
f3 = open('/Users/xiaolingyi/Documents/GitHub/CZ3005-AI-Lab/Lab1/Coord.json')
graph = json.load(f) # an adjacency list where the neighbor list of node ‘v’ 
energycost = json.load(f1)# energy cost between a pair of node (v, w)
dist = json.load(f2)# distance between a pair of node (v, w) 
coord = json.load(f3)# coordination of a node ‘v’ is a pair (X, Y) 
predecessor = {} # dictionary

def linear_heuristic(currentNode, endNode):
    starting_x = coord[currentNode][0]
    starting_y = coord[currentNode][1]
    ending_x = coord[endNode][0]
    ending_y = coord[endNode][1]
    #calculate the euclidean distance between the two coordinate 
    euclidean_distance = math.sqrt((starting_x - ending_x)**2 + (starting_y - ending_y)**2)
    return euclidean_distance

def updatedAStar (startnode,endnode,weight):
    # start timer for how long it take for A* program
    start_astar = timeit.default_timer()
    visited = set() # unordered unchangable unindexed and cannot have duplicate 
    q = PriorityQueue()
    predecessor[startnode] = 0
    for neighbour in graph[startnode]: # starting from startnode
        temp1 = str(neighbour)+','+str(startnode)
        totalenergy = energycost[temp1] # geting energy cost between neighbor and startnode
        distNext = dist[temp1] #the distance traveled so far
        heurDist = linear_heuristic(neighbour, endnode)# what is the eulidean distance of the node to endnode
        functionDist = distNext + heurDist
        q.put((functionDist, (startnode, neighbour), totalenergy, distNext)) # tuple comparison, functionDist is compaired first
    while q: # while the priority Queue is not exhaustive
        functionDist, (predecessornode, current), energy, traveldist = q.get()
        if current not in visited:  #if the new node have not been visit before
            predecessor[current] = predecessornode # store in dictionary as "current" : predecessornode
            if current == endnode: # find the shortest path
                stop_astar = timeit.default_timer()
                printshortestpath(startnode, endnode)
                print('Time: ', stop_astar - start_astar)
                return
            for neighbours in graph[current]: # loop though the an adjacency list of current
                temp = str(neighbours)+','+str(current)
                totalenergy = energy + energycost[temp]
                if neighbours not in visited and totalenergy <= 287932: # energy budget
                    visited.add(current)
                    distNext = dist[temp]
                    heurDist = linear_heuristic(neighbours, endnode)#what is the eulidean distance of the node to endnode
                    gdist = traveldist + distNext # the distance traveled so far
                    if gdist < heurDist: # if the distance traveled so far smaller then the estimated reaching distance( less then half way)
                        fdist = gdist + heurDist # functionalDist = distance traveled so far + huristic
                    else: # if nearing to rinding the end goal
                        fdist = (gdist+(2*weight-1)*heurDist)/weight
                    q.put((fdist, (current, neighbours), totalenergy, gdist))


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

# updatedAStar('1','50',1.13)
