import java.util.List;

public class Node {
    int N;
    String name;
    boolean visited;
    double distancetravelled;
    Long energyconsumed;

    Node(int n, double distancetravelled, Long energyconsumed){
        this.N = n;
        this.distancetravelled = distancetravelled;
        this.energyconsumed = energyconsumed;
    }
    void visit() {
        visited = true;
    }

    void unvisit() {
        visited = false;
    }
}