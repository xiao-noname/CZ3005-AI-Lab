public class Edge {
    int source;
    int destination;
    int distancetravelled;
    int energyconsumed;

    Edge(int source, int destination, int distancetravelled, int energyconsumed)
    {
        this.source = source;
        this.destination = destination;
        this.distancetravelled = distancetravelled;
        this.energyconsumed = energyconsumed;
    }
}
