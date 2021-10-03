import Q1
import Q2actual
import Q3
import json

f = open('Lab1\G.json',)
f1 = open('Lab1\Cost.json')
f2 = open('Lab1\Dist.json')
f3 = open('Lab1\Coord.json')
graph = json.load(f)
energycost = json.load(f1)
dist = json.load(f2)
coord = json.load(f3)

print("|| Task 1: Breadth First Search ||")
# Q1.bfs('1','50')

print("\n|| Task 2: Uniform Cost Search ||\n")
# Q2actual.ucs('1','50')

print("\n|| Task 3: A* Search ||\n")
Q3.updatedAStar('1', '50', graph, energycost, dist, coord)


