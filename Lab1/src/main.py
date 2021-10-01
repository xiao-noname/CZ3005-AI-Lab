import Q1
import Q2actual
import Q3

print("|| Task 1: Breadth First Search ||")
Q1.bfs('1','50')
Q1.printshortestpath('50')

print("\n|| Task 2: Uniform Cost Search ||\n")
Q2actual.ucs('1','50')
Q2actual.printshortestpath('1','50')

print("\n|| Task 3: A* Search ||\n")
Q3.updatedAStar('1', '50')
Q3.printshortestpath('1', '50')


