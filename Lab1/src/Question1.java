//using a modified version of BFS
//time complexity of O(v+e)
import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;

//Ask for the source node
//Ask for the target node
//You can assess the neighbours of the node using G['v']
public class Question1 {
    private static boolean BFS(ArrayList<ArrayList<Integer>> adj, int src,
    int dest, int v, int pred[], int dist[])
    {
    // a queue to maintain queue of vertices whose
    // adjacency list is to be scanned as per normal
    // BFS algorithm using LinkedList of Integer type
    LinkedList<Integer> queue = new LinkedList<Integer>();

    // boolean array visited[] which stores the
    // information whether ith vertex is reached
    // at least once in the Breadth first search
    boolean visited[] = new boolean[v];

    // initially all vertices are unvisited
    // so v[i] for all i is false
    // and as no path is yet constructed
    // dist[i] for all i set to infinity
    for (int i = 0; i < v; i++) {
        visited[i] = false;
        dist[i] = Integer.MAX_VALUE;
        pred[i] = -1;
    }

    // now source is first to be visited and
    // distance from source to itself should be 0
    visited[src] = true;
    dist[src] = 0;
    queue.add(src);

    // bfs Algorithm
    while (!queue.isEmpty()) {
    int u = queue.remove();
        for (int i = 0; i < adj.get(u).size(); i++) {
            if (visited[adj.get(u).get(i)] == false) {
            visited[adj.get(u).get(i)] = true;
            dist[adj.get(u).get(i)] = dist[u] + 1;
            pred[adj.get(u).get(i)] = u;
            queue.add(adj.get(u).get(i));

                // stopping condition (when we find
                // our destination)
                if (adj.get(u).get(i) == dest)
                    return true;
            }
        }
    }
    return false;
    }
    }

}
