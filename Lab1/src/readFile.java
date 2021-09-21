import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.text.ParseException;
import java.util.*;
import org.json.*;
import org.json.simple.*;
import org.json.simple.parser.JSONParser;

public class readFile {
    private int fileno;
    JSONParser parser = new JSONParser();
    JSONObject weightObject;
    JSONObject energyObject;
    JSONObject neighbourObject;
    public readFile(){
		try {
			Object NodeWeight = parser.parse(new FileReader("Lab1/Dist.json"));
            Object eCost = parser.parse(new FileReader("Lab1/Cost.json"));
            Object NeighbourList = parser.parse(new FileReader("Lab1/G.json"));
            weightObject = (JSONObject) NodeWeight;
            energyObject = (JSONObject) eCost;
            neighbourObject = (JSONObject) NeighbourList;
        }
        catch (Exception e) {
			e.printStackTrace();
        }
        
    }
    public void createEdges(List<Node>Nodelist, HashMap<Node, LinkedList<Node>> adjacencyMap)
    {
        Set keys = weightObject.keySet();
        Iterator a = keys.iterator();
        while(a.hasNext())
        {
            String b = (String) a.next();   //split the key and create edges
            System.out.println(b);
            System.out.println(energyObject.get(b));   //read in the energy file to get the cost
            System.out.println(weightObject.get(b));
            double weight = (double) weightObject.get(b);
            Long energy = (Long) energyObject.get(b);
            Node source = Nodelist.get(Integer.valueOf(b.split(",")[0]));
            Node destination = new Node(Integer.valueOf(b.split(",")[1]),weight,energy);
            LinkedList<Node> tmp = new LinkedList<>();
            tmp.add(destination);
            adjacencyMap.put(source,tmp);
        }
}
    
}
