//referenced from https://stackabuse.com/graphs-in-java-breadth-first-search-bfs/
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.PriorityQueue;

public class BFS {
    Node startNode;
    Node endNode;
    String path;
    double energycost;
    double distance;
    public void BFS(int start, int end, ArrayList<Node> Graph){
        startNode = Graph.get(start);
        endNode = Graph.get(end);
        if (startNode == null)
            return;
        if (start == end)
        {
            System.out.println("Shortest Path: S -> T");
            System.out.println("Shortest Distance: 0");
            System.out.println("Total Energy Cost: 0");
        }

    }
}
