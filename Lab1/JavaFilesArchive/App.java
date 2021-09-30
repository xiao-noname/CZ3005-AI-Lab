import java.util.*;

public class App {
    public HashMap<Node, LinkedList<Node>> adjacencyMap = new HashMap<>();
    public List<Node> NodeList = new ArrayList<Node>();
    public App(){
        generateallnodes();
        readFile rf = new readFile();
        rf.createEdges(NodeList,adjacencyMap);
    }
    public void generateallnodes(){
        //generate all nodes
        for(int i=0;i<264346;i++)
        {
            NodeList.add(new Node(i,(double)0,(long)0));
        }
        //System.out.println(nodelist.get(0).N);
    }
    public static void main(String[] args) throws Exception {
        
        App a = new App();
        
        System.out.println("Hello, World!");
    }
}
