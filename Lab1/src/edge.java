public class edge {
    private int source;
    private int destination;
    private int weight;
    private int energyCost;
    private boolean visited = false;
    public edge(int source, int destination, int weight){
        this.source = source;
        this.destination = destination;
        this.weight = weight;
    }
    public void setEnergy(int energyCost){
        this.energyCost = energyCost;
    }
    public void setSource(int source){
        this.source = source;
    }
    public void setDestination(int destination){
        this.destination = destination;
    }
    public void setDistance(int weight){
        this.weight = weight;
    }
    public int getSource(){
        return source;
    }
    public int getDestination(){
        return destination;
    }
    public int getEnergy(){
        return energyCost;
    }
    public int getDistance(){
        return weight;
    }
    public void setvVsited(boolean visited){
        this.visited = visited;
    }
    public boolean getVisited(){
        return visited;
    }
}
