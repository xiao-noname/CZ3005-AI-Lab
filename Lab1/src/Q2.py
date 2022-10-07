import json
import timeit
from queue import PriorityQueue
import os

f1 = open(os.path.join(os.path.dirname(__file__), 'data', 'Coord.json'))
f2 = open(os.path.join(os.path.dirname(__file__), 'data', 'Cost.json'))
f3 = open(os.path.join(os.path.dirname(__file__), 'data', 'Dist.json'))
f4 = open(os.path.join(os.path.dirname(__file__), 'data', 'G.json'))
coordData = json.load(f1)
energyData = json.load(f2)
distData = json.load(f3)
graphData = json.load(f4)
parent = {}

def ucs(start_node, end_node):
    visited = set()
    q = PriorityQueue()
    parent[start_node] = 0
    for neighbour in graphData[start_node]:
        node_set = neighbour +',' + start_node
        curr_energy = energyData[node_set]
        curr_dist = distData[node_set]
        q.put((curr_dist, (start_node, neighbour), curr_energy))
    while q:
        dist_travel,(parent_node,current),energy = q.get()
        if current not in visited:
            parent[current] = parent_node
            if current == end_node:
                printshortestpath(start_node, end_node, dist_travel, energy)
                return
            for neighbours in graphData[current]:
                node_pair = neighbours +','+ current
                curr_energy = energy + energyData[node_pair]
                if neighbours not in visited and curr_energy<=287932:
                    visited.add(current)
                    curr_dist = distData[node_pair] + dist_travel
                    parent[neighbours] = current
                    q.put((curr_dist, (current, neighbours), curr_energy))


def printshortestpath(start_node, end_node, currEnergy, currDist):
    shortest_path = [end_node]
    curr_node = end_node
    while (parent[curr_node] != start_node):
        shortest_path.insert(0, parent[curr_node])
        curr_node = parent[curr_node]
    shortest_path.insert(0,start_node)
    print("Shortest Path: \n Start: ", end = '')
    for i in range(len(shortest_path)-1):
        print(shortest_path[i]+" -> ", end = '')
    print(end_node + " End" )
    print("\nShortest Distance: %.2f" %currDist)
    print("Total Energy Cost: "+ str(currEnergy))



