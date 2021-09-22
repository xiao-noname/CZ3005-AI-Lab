import json
from queue import PriorityQueue

f = open('Lab1\G.json',)
f1 = open('Lab1\Cost.json')
f2 = open('Lab1\Dist.json')
graph = json.load(f)
energycost = json.load(f1)
dist = json.load(f2)

visited = set()
predecessor = {}
q = PriorityQueue()

def ucs (startnode,endnode):
    visited.add(startnode)
    q.put((0,startnode))
    predecessor[startnode]= [0,0,0]
    while not q.empty():
        traveldist,current = q.get()
        #print(m)
        #if current == endnode:
            #return
        for neighbours in graph[current]:
            temp = str(current)+','+str(neighbours)
            Adist = traveldist + dist[temp]
            Aenergy = predecessor[current][2] + energycost[temp]
            if neighbours not in visited and Aenergy < 287932:
                visited.add(neighbours)
                q.put((Adist,neighbours))
                predecessor[neighbours] = [current,Adist,Aenergy]
                if neighbours == endnode:
                    return

def printshortestpath(endnode):
    shortestpath = []
    shortestpath.append(endnode)
    movement = endnode
    while (predecessor[movement][0] != 0):
        shortestpath.insert(0, predecessor[movement][0])
        movement = predecessor[movement][0]

    print(shortestpath)
    print(len(shortestpath))
    print(predecessor[50][1])

ucs('1','50')
printshortestpath('50')