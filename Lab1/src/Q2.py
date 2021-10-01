import json
from queue import PriorityQueue

f = open('Lab1\G.json',)
f1 = open('Lab1\Cost.json')
f2 = open('Lab1\Dist.json')
graph = json.load(f)
energycost = json.load(f1)
dist = json.load(f2)


predecessor = {}


def ucs (startnode,endnode):
    #visited = set()
    q = PriorityQueue()
    #visited.add(startnode)
    #q.put((0,(startnode,startnode)))
    predecessor[startnode]= [0,0,0] #predecessor,accumulatedEnergy
    for neighbours in graph[startnode]:
        temp2 = str(startnode)+','+str(neighbours)
        Adist = dist[temp2]
        Aenergy = energycost[temp2]
        q.put((Adist,(neighbours,startnode)))
    while not q.empty():
        traveldist,(current,predecessornode) = q.get()
        #visited.add(current)
        temp1 = str(predecessornode)+','+str(current)
        Tdist = predecessor[predecessornode][1] + dist[temp1]
        Tenergy = predecessor[predecessornode][2] + energycost[temp1]
        predecessor[current]= [predecessornode,Tdist,Tenergy]
        if current == endnode:
            print("i did it")
            return
        for neighbours in graph[current]:
            temp = str(current)+','+str(neighbours)
            Adist = traveldist + dist[temp]
            Aenergy = predecessor[current][2] + energycost[temp]

            if neighbours not in predecessor.keys():
                if Aenergy <= 287932:
                    q.put((Adist,(neighbours,current)))
                    print(neighbours)
                    if (neighbours == '50'):
                        print("i did it")
                        break
                    

def printshortestpath(endnode):
    shortestpath = []
    shortestpath.append(endnode)
    movement = endnode
    while (predecessor[movement][0] != 0):
        shortestpath.insert(0, predecessor[movement][0])
        movement = predecessor[movement][0]

    print(shortestpath)
    print(len(shortestpath))
    print(predecessor['50'])

# ucs('1','50')
# printshortestpath('50')